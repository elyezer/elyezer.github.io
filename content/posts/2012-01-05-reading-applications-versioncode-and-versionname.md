+++
title = "Reading application's versionCode and versionName"
date = "2012-01-05 14:45:00"
category = "Android Tips"
tags = ["android", "development", "code", "snippet"]
slug = "reading-applications-versioncode-and-versionname"
+++

When versioning your application, you use the `AndroidManifest.xml` to specify
the *versionCode* and *versionName*.

You can read your application's *versionCode* and *versionName* from you
activity using the following code:

```java
PackageInfo packageInfo = getPackageManager().getPackageInfo(getPackageName(), 0);
int versionNumber = packageInfo.versionCode;
String versionName = packageInfo.versionName;
```

To know more about versioning your app read de
[documentation](http://developer.android.com/guide/publishing/versioning.html).
