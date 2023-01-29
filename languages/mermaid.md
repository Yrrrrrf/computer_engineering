# [Mermaid](https://mermaidjs.github.io/)

Mermaid is a simple $markdown-like$ [[script language]] for **generating charts and [[uml|diagrams]] from text via [[javascript]]**. It's great for quickly sketching out diagrams for documentation.

## Usage
[[flow diagram]]
```mermaid
graph TD
    A[Client] --> B[Load Balancer]
    B --> C[Server01]
    B --> D[Server02]
```

### [class diagram](https://mermaid.js.org/syntax/classDiagram.html)
[[class diagram]]
Is a type of static structure diagram that describes the structure of a system by showing the system's classes, their attributes, operations (or methods), and the relationships among objects.
```mermaid
---
title: Animal example
---
classDiagram
    note "From Duck till Zebra"
    Animal <|-- Duck
    note for Duck "can fly\ncan swim\ncan dive\ncan help in debugging"
    Animal <|-- Fish
    Animal <|-- Zebra
    Animal : +int age
    Animal : +String gender
    Animal: +isMammal()
    Animal: +mate()
    class Duck{
        +String beakColor
        +swim()
        +quack()
    }
    class Fish{
        -int sizeInFeet
        -canEat()
    }
    class Zebra{
        +bool is_wild
        +run()
    }
```


### References
- [usage example (video)](https://www.youtube.com/watch?v=Tsu02d6Qti0)
- [Mermaid Documentation](https://mermaidjs.github.io/)
- [Mermaid Live Editor](https://mermaidjs.github.io/mermaid-live-editor/)

