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

()  # group -> (ab)+
[]  # range -> [a-z] 
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
# EXAMPLES:

- returns begins with a and finish with a: `a.*a`
- returns strings even numbers at the last position: `[0-9]*[02468]`
- get an hout format 00:00:00
    - 24hr `(([0-1][0-9])|([2][0-3])):[0-5][0-9]:[0-5][0-9]`
    - 12hr) `()`
- get any valid date (according to the month) in the  format dd/mm/yy: `[0-9][0-9]\/(((0[13578]|1[02])\/([0-2][0-9]|3[01]))|((0[469]|1[1])\/([0-2][0-9]|30))|(02\/([0-1][0-9]|2[0-8])))`
- get any mail: `[\w\.\-]{2,}@\w{2,}\.[a-z]{2,4}`
- get any url: `https?:\/\/[\w\.\-]+\.[a-z]{2,4}`


### regex to a finite automata
- There is a program that converts a regex to a deterministic finite automata (DFA)
steps:
1. create a regex
2. convert the regex to a NFA
3. convert the NFA to a DFA
4. convert the DFA to a table
5. convert the table to a program



 