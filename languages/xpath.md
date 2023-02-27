# [XPath](https://www.w3schools.com/xml/xpath_intro.asp)

XPath is a [[script language|language]] for selecting nodes from an `XML` document using **path expressions** to navigate in XML documents.

Is like the equivalent of a [[languages/regular expressions|regular expression]] for [[XML]] documents.

It's usually used to [[web scrapping|extract data from XML documents]] in a [[web]] page. 

## XPath Syntax

XPath uses path expressions to select nodes in an XML document. The path expression is a sequence of steps separated by slashes. Each step is a test of a node in the tree. The following example selects all `p` elements that are children of a `div` element:

```xml
<div>
  <p>Paragraph 1</p>
  <p>Paragraph 2</p>
</div>
```

The path expression to select all `p` elements is:

```xml
/div/p
```

## XPath Axes

XPath uses axes to navigate the XML document. The following table lists the most important axes:
- `ancestor`: Selects all ancestors of the current node.
- `ancestor-or-self`: Selects all ancestors of the current node, and the current node itself.
- `attribute`: Selects all attributes of the current node.
- `child`: Selects all children of the current node.
- `descendant`: Selects all descendants of the current node.
- `Sself`: Selects all descendants of the current node, and the current node itself.
- `following`: Selects everything in the document after the closing tag of the current node.
- `following-sibling`: Selects all siblings after the current node.
- `namespace`: Selects all namespace nodes of the current node.
- `parent`: Selects the parent of the current node.
- `preceding`: Selects everything in the document before the opening tag of the current node.
- `preceding-sibling`: Selects all siblings before the current node.
- `self`: Selects the current node.

## XPath Functions

XPath contains a number of functions to use in path expressions. The following table lists the most important functions:
- `last()`: Returns the index of the last node in the node set.
- `position()`: Returns the position of the current node in the node set.
- `count()`: Returns the number of nodes in the node set.
- `id()`: Returns the node set with the given id.
- `local-name()`: Returns the local part of the name of the current node.
- `namespace-uri()`: Returns the URI of the namespace of the current node.
- `name()`: Returns the name of the current node.
- `string()`: Converts the current node to a string.
- `concat()`: Returns the concatenation of two or more strings.
- `starts-with()`: Returns true if the first string starts with the second string.
- `contains()`: Returns true if the first string contains the second string.
- `substring-before()`: Returns the substring before the first occurrence of a string.
- `substring-after()`: Returns the substring after the first occurrence of a string.
- `substring()`: Returns a substring of a string.
- `string-length()`: Returns the length of a string.
- `normalize-space()`: Returns the string with whitespace normalized by stripping leading and trailing whitespace and replacing sequences of whitespace characters by a single space.
- `translate()`: Returns the string resulting from replacing all occurrences of one substring with another.
- `boolean()`: Converts the current node to a boolean.
- `not()`: Returns true if the argument is false.
- `true()`: Returns true.
- `false()`: Returns false.
- `lang()`: Returns true if the language of the current node is the same as the language specified in the argument.
- `number()`: Converts the current node to a number.
- `sum()`: Returns the sum of a node set. 
- `floor()`: Returns the largest integer less than or equal to the argument.
- `ceiling()`: Returns the smallest integer greater than or equal to the argument.
- `round()`: Returns the number rounded to the nearest integer.
- `abs()`: Returns the absolute value of a number.
- `round-half-to-even()`: Returns the number rounded to the nearest integer, with half-way cases rounded to the nearest even integer.
- `codepoints-to-string()`: Returns the string resulting from converting the argument to a sequence of Unicode code points.


# USE XPATH GO GET A PRE TAG
```xpath
$x('//pre/text()').map(x => x.wholeText)  # using js
```
