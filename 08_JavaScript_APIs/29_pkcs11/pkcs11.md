[\n

\n

The `pkcs11` API enables an extension to enumerate [PKCS
#11](https://en.wikipedia.org/wiki/PKCS_11) security modules, and to make them
accessible to the browser as sources of keys and certificates.

\n

To use this API you need to have the "pkcs11" [permission](/en-US/docs/Mozilla
/Add-ons/WebExtensions/manifest.json/permissions).

\n

## Provisioning PKCS #11 modules

\n

There are two environmental prerequisites for using this API:

\n

\n

  * one or more PKCS #11 modules must be installed on the user's computer
\n

  * for each installed PKCS #11 module, there must be a JSON manifest file that enables the browser to locate the module.
\n

\n

Most probably, the user or device administrator would install the PKCS #11
module, and its installer would install the manifest file at the same time.
Note, though, that the module and manifest can't be installed as part of the
extension's own installation process.

\n

For details about the manifest file's contents and location, see [Native
manifests](/en-US/docs/Mozilla/Add-ons/WebExtensions/Native_manifests).

\n

## Functions

\n

\n[`pkcs11.getModuleSlots()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pkcs11/getModuleSlots "Enumerate a module's slots. This
function returns an array containing one entry for each slot. Each entry
contains the slot's name and, if the slot contains a token, information about
the token.")

\n    For each slot in a module, get its name and whether it contains a token.

\n[`pkcs11.installModule()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pkcs11/installModule "Installs the named PKCS #11
module, making it available to Firefox.")

\n    Installs the named PKCS #11 module.

\n[`pkcs11.isModuleInstalled()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pkcs11/isModuleInstalled "Checks whether the named PKCS
#11 module is currently installed in Firefox.")

\n    Checks whether the named PKCS #11 module is installed.

\n[`pkcs11.uninstallModule()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pkcs11/uninstallModule "Uninstalls the named PKCS #11
module from Firefox.")

\n    Uninstalls the named PKCS #11 module.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`getModuleSlots`| \n No| \n No| 58| \n No| \n No  
`installModule`| \n No| \n No| 58| \n No| \n No  
`isModuleInstalled`| \n No| \n No| 58| \n No| \n No  
`uninstallModule`| \n No| \n No| 58| \n No| \n No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`getModuleSlots`

Non-standard __

| \n No support\n\n No| \nNo support\n\n No| \nFull support\n\n 58| \nNo
support\n\n No| \nNo support\n\n No  
`installModule`

Non-standard __

| \n No support\n\n No| \nNo support\n\n No| \nFull support\n\n 58| \nNo
support\n\n No| \nNo support\n\n No  
`isModuleInstalled`

Non-standard __

| \n No support\n\n No| \nNo support\n\n No| \nFull support\n\n 58| \nNo
support\n\n No| \nNo support\n\n No  
`uninstallModule`

Non-standard __

| \n No support\n\n No| \nNo support\n\n No| \nFull support\n\n 58| \nNo
support\n\n No| \nNo support\n\n No  
  
\n]

  *[\nFull support\n]: Full support
  *[ Non-standard __]: Non-standard. Expect poor cross-browser support.
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[\nNo support\n]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Non-standard __]: Non-standard. Expect poor cross-browser support.
  *[\n No support\n]: No support
  *[Chrome __]: Chrome

