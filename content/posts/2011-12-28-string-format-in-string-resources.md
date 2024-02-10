+++
title = "String format in String Resources"
date = "2011-12-28 19:36:00"
category = "Android Tips"
tags = ["android", "development", "resources"]
slug = "string-format-in-string-resources"
+++

The string format, when added to string.xml resource, has a differente syntax,
for exemple:

```java
Hello, %s! You have %d new messages.
```

Becomes:

```java
Hello, %1$s! You have %2$d new messages.
```

The syntax is: `*%<position>$<type>*`. where `<position>` starts at 1 and type
is the Java String format like **d**, **s**, **f**.

Source: [String
Resources](http://developer.android.com/guide/topics/resources/string-resource.html)
