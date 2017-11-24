[



The `pkcs11` API enables an extension to enumerate [PKCS
#11](https://en.wikipedia.org/wiki/PKCS_11) security modules, and to make them
accessible to the browser as sources of keys and certificates.



To use this API you need to have the "pkcs11" [permission](/en-US/docs/Mozilla
/Add-ons/WebExtensions/manifest.json/permissions).



## Provisioning PKCS #11 modules



There are two environmental prerequisites for using this API:





  * one or more PKCS #11 modules must be installed on the user's computer


  * for each installed PKCS #11 module, there must be a JSON manifest file that enables the browser to locate the module.




Most probably, the user or device administrator would install the PKCS #11
module, and its installer would install the manifest file at the same time.
Note, though, that the module and manifest can't be installed as part of the
extension's own installation process.



For details about the manifest file's contents and location, see [Native
manifests](/en-US/docs/Mozilla/Add-ons/WebExtensions/Native_manifests).



## Functions



[`pkcs11.getModuleSlots()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pkcs11/getModuleSlots "Enumerate a module's slots. This
function returns an array containing one entry for each slot. Each entry
contains the slot's name and, if the slot contains a token, information about
the token.")

    For each slot in a module, get its name and whether it contains a token.

[`pkcs11.installModule()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pkcs11/installModule "Installs the named PKCS #11
module, making it available to Firefox.")

    Installs the named PKCS #11 module.

[`pkcs11.isModuleInstalled()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pkcs11/isModuleInstalled "Checks whether the named PKCS
#11 module is currently installed in Firefox.")

    Checks whether the named PKCS #11 module is installed.

[`pkcs11.uninstallModule()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pkcs11/uninstallModule "Uninstalls the named PKCS #11
module from Firefox.")

    Uninstalls the named PKCS #11 module.



## Browser compatibility



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`getModuleSlots`|  No|  No| 58|  No|  No  
`installModule`|  No|  No| 58|  No|  No  
`isModuleInstalled`|  No|  No| 58|  No|  No  
`uninstallModule`|  No|  No| 58|  No|  No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`getModuleSlots`

Non-standard __

|  No support No| No support No| Full support 58| No
support No| No support No  
`installModule`

Non-standard __

|  No support No| No support No| Full support 58| No
support No| No support No  
`isModuleInstalled`

Non-standard __

|  No support No| No support No| Full support 58| No
support No| No support No  
`uninstallModule`

Non-standard __

|  No support No| No support No| Full support 58| No
support No| No support No  
  
]

  *[Full support]: Full support
  *[ Non-standard __]: Non-standard. Expect poor cross-browser support.
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[No support]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Non-standard __]: Non-standard. Expect poor cross-browser support.
  *[ No support]: No support
  *[Chrome __]: Chrome

