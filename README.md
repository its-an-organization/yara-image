# yara-image

This repo builds an image which has a functional yara scanner in it.  It also downloads and compiles the free rules from https://github.com/reversinglabs/reversinglabs-yara-rules.git.  These rules were not chosen for any reason other than they are free and demonstrate the ability to compile rules successfully.  The builds should be modified to compile the specific set of rules that you are interested in.  

The intent of this teask is to be used in a future tekton task definition for scanning built images for malware using Yara.



