# Regular Expressions (RegEx)

Regular expressions are a powerful tool for matching patterns in text. They are used in many programming languages, and are often used in text editors and text processing tools.

```bash
.  # character
..  # string of n characters

^a  # matches the beginning of a string
$a  # matches the end of a string 

[a]  # character in the brackets
[^a]  # character not in the brackets

a+  # string that contains one or more "a" characters
a*  # string that contains zero or more "a" characters
a?  # string that contains zero or one "a" characters

a{5}  # string that contains five consecutive "a" characters
a{2,5}  # string that contains two to five consecutive "a" characters

(ab)+  # string that contains one or more occurrences of the string "ab"

a|b  # string that contains "a" or "b"

\*  # matches the string "*"

/d  # matches any digit
/D  # matches any character except a digit

/s  # matches any whitespace character
/S  # matches any character except a whitespace character

/w  # matches any alphanumeric character
/W  # matches any character except an alphanumeric character

()  # group
[]  # range
[^]  # not range
```

| regex | meaning|
| - | - |
| `.` | $char$ | 
| `/d` | $0:9$ |
| `/w` | $word$ |
| `/s` | $whitespace$ |
| `a\|b` | `a` $or$ `b` char |
| `()` | $group$ |
| `[]` | $range$ |
| `[^]` | $not range$ |
| `\` | invert | character that is not a digit |
| `^` | $beginning$ |
| `$` | $end$ |
| `*` | $\=>0$ |
| `+` | $\=>1$ |
| `?` | $0 \| 1$ |
| `[n]` | specific digit |
| `[0-9a-zA-Z]` | specific word character | character that is a digit or a letter from A to Z |
| `[a-zA-Z]` | a | uppercase or lowercase letter |
| `{n}` | specific number | character that is exactly n times in a row |
| `{a,b}` | range of numbers | character that is between a and b times in a row |
| `{a,}` | at least a | character that is at least a times in a row |
| `{,b}` | at most b | character that is at most b times in a row |
| `[a-z]` | range | lowercase letter from a to z |
| `[A-Z]` | range | uppercase letter from A to Z |
| `[a-zA-Z]` | range | uppercase or lowercase letter |
| `[0-9a-zA-Z]` | range | character that is a digit or a letter from A to Z |


- `url`: https?:\/\/[\w\.\-]+\.[a-z]{2,4}
- `mail`: [\w\.\-]{2,}@\w{2,}\.[a-z]{2,4}

----
## Basic Patterns

The simplest regular expressions are single characters. They match themselves. For example, the regular expression `a` matches the string `a` but not the string `b`. The regular expression `b` matches the string `b` but not the string `a`.

Regular expressions can also match a range of characters. For example, the regular expression `[abc]` matches the string `a`, the string `b`, or the string `c`. The regular expression `[a-z]` matches any lowercase letter. The regular expression `[0-9]` matches any digit.

Regular expressions can also match any character except a specific set of characters. For example, the regular expression `[^abc]` matches any character except `a`, `b`, or `c`. The regular expression `[^0-9]` matches any character except a digit.

## Repetition

Regular expressions can also match repeated characters. For example, the regular expression `a*` matches any string that contains zero or more `a` characters. The regular expression `a+` matches any string that contains one or more `a` characters. The regular expression `a?` matches any string that contains zero or one `a` characters. The regular expression `a{5}` matches any string that contains five consecutive `a` characters. The regular expression `a{2,5}` matches any string that contains two to five consecutive `a` characters.

## Grouping

Regular expressions can also match groups of characters. For example, the regular expression `(ab)+` matches any string that contains one or more occurrences of the string `ab`.

## Alternation

Regular expressions can also match one of several patterns. For example, the regular expression `a|b` matches the string `a` or the string `b`.

## Escaping

Regular expressions can also match special characters. For example, the regular expression `\*` matches the string `*`. The regular expression `\\` matches the string `\`. The regular expression `\(` matches the string `(`. The regular expression `\)` matches the string `)`. The regular expression `\|` matches the string `|`. The regular expression `\.` matches the string `.`. The regular expression `\?` matches the string `?`. The regular expression `\+` matches the string `+`. The regular expression `\*` matches the string `*`. The regular expression `\{` matches the string `{`. The regular expression `\}` matches the string `}`. The regular expression `\[` matches the string `[`. The regular expression `\]` matches the string `]`. The regular expression `\^` matches the string `^`. The regular expression `\$` matches the string `$`. The regular expression `\d` matches any digit. The regular expression `\D` matches any character except a digit. The regular expression `\s` matches any whitespace character. The regular expression `\S` matches any character except a whitespace character. The regular expression `\w` matches any alphanumeric character. The regular expression `\W` matches any character except an alphanumeric character.

## Anchors

Regular expressions can also match the beginning or end of a string. For example, the regular expression `^a` matches any string that starts with the character `a`. The regular expression `a$` matches any string that ends with the character `a`.

## Examples

The regular expression `a*` matches any string that contains zero or more `a` characters. For example, it matches the strings `a`, `aa`, `aaa`, `aaaa`, and so on. It also matches the empty string.

The regular expression `a+` matches any string that contains one or more `a` characters. For example, it matches the strings `a`, `aa`, `aaa`, `aaaa`, and so on. It does not match the empty string.

The regular expression `a?` matches any string that contains zero or one `a` characters. For example, it matches the strings `a`, `aa`, `aaa`, `aaaa`, and so on. It also matches the empty string.

The regular expression `a{5}` matches any string that contains five consecutive `a` characters. For example, it matches the strings `aaaaa`, `aaaaaa`, `aaaaaaa`, and so on. It does not match the strings `a`, `aa`, `aaa`, `aaaa`, or the empty string.

The regular expression `a{2,5}` matches any string that contains two to five consecutive `a` characters. For example, it matches the strings `aa`, `aaa`, `aaaa`, `aaaaa`, `aaaaaa`, `aaaaaaa`, and so on. It does not match the strings `a`, or the empty string.

The regular expression `(ab)+` matches any string that contains one or more occurrences of the string `ab`. For example, it matches the strings `ab`, `abab`, `ababab`, `abababab`, and so on. It does not match the strings `a`, `b`, `aa`, `bb`, `aab`, `abb`, `baa`, `bab`, `aba`, `abb`, `baa`, `bab`, `bba`, `bbb`, or the empty string.

The regular expression `a|b` matches the string `a` or the string `b`. For example, it matches the strings `a`, `b`, `aa`, `ab`, `ba`, `bb`, `aaa`, `aab`, `aba`, `abb`, `baa`, `bab`, `bba`, `bbb`, and so on. It does not match the empty string.

