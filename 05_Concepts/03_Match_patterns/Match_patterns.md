匹配模式是一种指定URL组的方法：匹配模式匹配特定的一组URL。 它们是在几个地方使用WebExtensions API进行的扩展，最显着的是指定将[内容脚本](/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts)加载到哪些文档中，并指定哪些URL添加[webRequest](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest)监听器。


使用匹配模式的API通常接受匹配模式列表，并且如果URL匹配任何模式，将执行适当的操作. 查看 manifest.json 中的[content_scripts](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/content_scripts)

## 匹配模式结构

所有的匹配模式选定的字符串。 除了特殊["<all_urls>"](/en-US/Add-ons/WebExtensions/Match_patterns#%3Call_urls%3E)模式外，匹配模式由三部分组成：_scheme_，_host_和_path_。 方案和主机由“：//”分隔。

    <方案>://<主机><路径>

### 方案

_scheme_ 有两种格式:

格式 | 匹配  
---|---  
"*" |  "http"  "https".  
One of "http", "https", "file", "ftp", "app". | 只匹配其中之一
  
### 主机

_host_ 有两种格式:

格式 | 匹配  
---|---  
"*" | 匹配任意的域名.  
"*." 剩余的主机名部分. | 指定的子域名 
完成的没有通配符的主机名 | 只匹配指定的.  
  
_host_ 当 _scheme_ 是file时候

请注意，通配符只能出现在开头。

### 路径
路径的开头一定是"/".

之后，它可能会包含任何“* ” 通配符和URL路径中允许的任何字符的组合。 与_host_不同，_path_ 组件可能在中间或末尾包含“* ”通配符，“ * ”通配符可能会多次出现。

### <all_urls>

特殊值“<all_urls>”匹配任何支持的方案下的所有URL：即“http”，“https”，“file”，“ftp”，“app”。

示例表格不进行翻译

### 无效的模式匹配

无效的模式 | 原因  
---|---  
`resource://path/` | 不支持的方案.  
`https://mozilla.org` | 没有路径.  
`https://mozilla.*.org/` | "*" 必须在开头.  
`https://*zilla.org/` | "*"在主机部分紧跟着的必须是 ".".  
`http*://mozilla.org/` | 方案部分只能是字符.  
`file://*` | 没有路径 应该是`file:///*`".  
  
## Testing match patterns

在编写扩展时，通常不直接使用匹配模式：通常将匹配模式字符串传递给API，API构造匹配模式并使用它来测试URL。 但是，如果您正在尝试确定使用哪种匹配模式，或者使用某种匹配模式进行调试，那么直接创建并测试匹配模式会很有用。 本节介绍如何做到这一点。

首先，打开开发人员工具设置并检查标记为“启用浏览器chrome和附加调试工具箱”的设置：

接下来，打开“浏览器控制台”：

这给你一个命令行，你可以使用它来在Firefox中执行特权JavaScript。

由于在浏览器控制台中运行的代码具有系统特权，因此无论何时使用它来运行代码，都需要准确理解代码的作用。这包括本文中的代码示例。

现在将这段代码粘贴到命令行并按下回车键：
    
    Cu.import("resource://gre/modules/MatchPattern.jsm");
    Cu.import("resource://gre/modules/BrowserUtils.jsm");

这有两点：

   *导入“MatchPattern.jsm”：这是实现匹配模式的系统模块。 具体来说，模块包含一个`MatchPattern`对象的构造函数。 MatchPattern对象定义了一个名为`matches（）的函数，它接受一个URI并返回“true”或“false”。
   *导入“BrowserUtils.jsm”：这包括一个`makeURI（）`函数，它将字符串转换为`[nsIURI](/en-US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIURI)。`nsIURI`是'matches（）`预期接收的类型。

现在你可以构造`MatchPattern`对象，构造URI，并检查URI是否匹配：
        
    var match = new MatchPattern("*://mozilla.org/");
    
    var uri = BrowserUtils.makeURI("https://mozilla.org/");
    match.matches(uri); //        < true
    
    uri = BrowserUtils.makeURI("https://mozilla.org/path");
    match.matches(uri); //        < false

## 转换模式匹配到正则

所有的匹配模式都可以用正则表达式来表示。 此代码将匹配模式转换为正则表达式：

    /**
     * Transforms a valid match pattern into a regular expression
     * which matches all URLs included by that pattern.
     *
     * @param  {string}  pattern  The pattern to transform.
     * @return {RegExp}           The pattern's equivalent as a RegExp.
     * @throws {TypeError}        If the pattern is not a valid MatchPattern
     */
    function matchPatternToRegExp(pattern) {
        if (pattern === '') {
            return (/^(?:http|https|file|ftp|app):\/\//);
        }
    
        const schemeSegment = '(\\*|http|https|file|ftp)';
        const hostSegment = '(\\*|(?:\\*\\.)?(?:[^/*]+))?';
        const pathSegment = '(.*)';
        const matchPatternRegExp = new RegExp(
            `^${schemeSegment}://${hostSegment}/${pathSegment}$`
        );
    
        let match = matchPatternRegExp.exec(pattern);
        if (!match) {
             throw new TypeError(`"${pattern}" is not a valid MatchPattern`);
        }
    
        let [, scheme, host, path] = match;
        if (!host) {
            throw new TypeError(`"${pattern}" does not have a valid host`);
        }
    
        let regex = '^';
    
        if (scheme === '*') {
            regex += '(http|https)';
        } else {
            regex += scheme;
        }
    
        regex += '://';
    
        if (host && host === '*') {
            regex += '[^/]+?';
        } else if (host) {
            if (host.match(/^\*\./)) {
                regex += '[^/]*?';
                host = host.substring(2);
            }
            regex += host.replace(/\./g, '\\.');
        }
    
        if (path) {
            if (path === '*') {
                regex += '(/.*)?';
            } else if (path.charAt(0) !== '/') {
                regex += '/';
                regex += path.replace(/\./g, '\\.').replace(/\*/g, '.*?');
                regex += '/?';
            }
        }
    
        regex += '$';
        return new RegExp(regex);
    }
    

