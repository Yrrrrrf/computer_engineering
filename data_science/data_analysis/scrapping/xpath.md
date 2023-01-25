# [XPath](https://www.w3schools.com/xml/xpath_intro.asp)

XPath is a [[script language|language]] for selecting nodes from an `XML` document using **path expressions** to navigate in XML documents.

It's usually used to [[scrapping|extract data from XML documents]] in a [[web]] page. 

## XPath Syntax

XPath uses path expressions to select nodes in an XML document. The path expression is a sequence of steps separated by slashes. Each step is a test of a node in the tree. The following example selects all `p` elements that are children of a `div` element:

```xml
<div>
  <p>Paragraph 1</p>
  <p>Paragraph 2</p>
</div>
```