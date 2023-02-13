# HyperText Markup Language

Is a language that describes the structure of a [[web]] page.

## [Base HTML structure](/languages/web/html/index.html)

The main html document usually had the name `index.html` and is the first file that is loaded when you open a website.

```html
<!DOCTYPE html>  <!-- doctype declaration -->
<html lang="en">  <!-- root element -->

    <head>  <!-- head element (metadata) -->
        <meta charset="UTF-8">  <!-- meta element (charset) -->
        <meta http-equiv="X-UA-Compatible" content="IE=edge">  <!-- force IE to use the latest rendering engine -->
        <meta name="viewport" content="width=device-width, initial-scale=1.0">  <!-- viewport -->
        <title>Document Title</title>  <!-- tab title -->
    </head>

    <body>
        Document content...
    </body>
</html>
```

## [HTML elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)

The elements are the building blocks of the html document.

```html
<h1>Heading content...</h1>  <!-- heading -->

<p>Paragraph content...</p>  <!-- paragraph -->

<ul>  <!-- unordered list -->
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ul>

<ol>  <!-- ordered list -->
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ol>
```

## [HTML attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes)

The attributes are used to add extra information to the elements.

```html
<a href="https://www.google.com">Link content...</a>  <!-- link -->

<img src="image.png" alt="Image description" width="480" height="240">  <!-- image -->
```

