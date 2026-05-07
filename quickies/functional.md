---
marp: true
size: 16:9
theme: uncover
class: invert
paginate: true
math: katex
style: |
  @import 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/fontawesome.min.css';
  @import 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/solid.min.css';

  a {
    font-size: 17pt;
  }

  table {
    margin: 0 25px 25px 15px;
  }

  tbody {
    width: 100%;
  }

  .my-small-size {
    font-size: 8pt;
    margin: 0px;
    padding: 0px;
  }
  
  .my-medium-size {
    font-size: 12pt;
    margin: 0px;
    padding: 0px;
  }

  ul li {
    font-size: 20pt;
  }
  
  ul li ul li {
    font-size: 17pt;
  }

  blockquote {
    font-size: 18pt;
  }

  footer {
    left: auto;
    right: auto;
    top: auto;
    bottom: auto;

    right: 20px;
    top: 20px;
  }

  .code-container {
    position: relative;
    margin: 0.1em 0;
  }
  
  .code-container pre {
    margin: 0;
    padding: 0.1em;
    background-color: #f5f5f5;
    border: 1px solid #ddd;
    border-radius: 4px;
    overflow-x: auto;
  }

  code {
    font-size: 0.5em;
  }

  .run-icon {
    position: absolute;
    top: 0.5em;
    right: 0.5em;
    color: white;
    font-size: 12pt;
    text-decoration: none;
    z-index: 10;
    transition: color 0.2s ease;
  }

  .run-icon:hover {
    color: lightgreen;
  }

  .timer-widget {
    position: fixed;
    top: 12px;
    right: 12px;
    width: 180px;
    height: 80px;
    font-family: monospace;
    background: #1a1a2e;
    border-radius: 8px;
    z-index: 9999;
    user-select: none;
  }

  .timer-display {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 28px;
    color: #0f0;
    transition: opacity .2s;
  }

  .timer-controls {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    opacity: 0;
    transition: opacity .2s;
    background: rgba(26, 26, 46, .85);
    border-radius: 8px;
  }

  .timer-widget:hover .timer-controls { opacity: 1; }
  .timer-widget:hover .timer-display  { opacity: .15; }

  .timer-min, .timer-sec {
    width: 36px;
    height: 28px;
    text-align: center;
    background: #0d0d1a;
    color: #0f0;
    border: 1px solid #0f0;
    border-radius: 4px;
    font: 16px monospace;
  }

  .timer-controls span {
    color: #0f0;
    font-size: 16px;
  }

  .timer-btn {
    padding: 4px 10px;
    font: bold 13px monospace;
    background: #0f0;
    color: #1a1a2e;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    min-width: 32px;
  }

  .timer-btn:hover {
    filter: brightness(1.2);
  }

  .timer-pause {
    display: none;
    background: #fa0;
  }
  
---

# Functional (Style)

### Quentin Crain

<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true, theme: 'default', securityLevel: 'loose', });
</script>

---

```python
nums = [4, 2, 7, 22]
```

---

New list where each number in `nums` except 7, which is thrown out, is incremented by 3.

<br/>

<table width="100%">

<tr>
    <th width="50%">Before</th>
    <th width="50%">After</th>
</tr>

<tr>

<td>

```python
nums = [4, 2, 7, 22]
```

</td>

<td>

```python
def add(a, b):
    return a + b

nums = [4, 2, 7, 22]

new_nums = []

for num in nums:
    if num != 7:
        new_nums.append(add(3, num))

return new_nums
```

</td>

</tr>

</table>

---

`3,` is added cognitive load in `add(3, num)`, lets get rid of it!

<br/>

<table width="100%">

<tr>
    <th width="50%">Before</th>
    <th width="50%">After</th>
</tr>

<tr>

<td>

```python
def add(a, b):
    return a + b

nums = [4, 2, 7, 22]

new_nums = []

for num in nums:
    if num != 7:
        new_nums.append(add(3, num))

return new_nums
```

</td>

<td>

```python
!import functools

def add(a, b):
    return a + b
!add_3 = functools.partial(add, 3)

nums = [4, 2, 7, 22]

new_nums = []

for num in nums:
    if num != 7:
!        new_nums.append(add_3(num))

return new_nums
```

</td>

</tr>

</table>

---

Simple `for` loops should be list comprehensions.

<br/>

<table width="100%">

<tr>
    <th width="50%">Before</th>
    <th width="50%">After</th>
</tr>

<tr>

<td>

```python
import functools

def add(a, b):
    return a + b
add_3 = functools.partial(add, 3)

nums = [4, 2, 7, 22]

new_nums = []

for num in nums:
    if num != 7:
        new_nums.append(add_3(num))

return new_nums
```

</td>

<td>

```python
import functools

def add(a, b):
    return a + b
add_3 = functools.partial(add, 3)

nums = [4, 2, 7, 22]

!new_nums = [add_3(num) for num in nums if num != 7]

return new_nums
```

</td>

</tr>

</table>

---

Make condition a function.

<br/>

<table width="100%">

<tr>
    <th width="50%">Before</th>
    <th width="50%">After</th>
</tr>

<tr>

<td>

```python
import functools

def add(a, b):
    return a + b
add_3 = functools.partial(add, 3)

nums = [4, 2, 7, 22]

new_nums = [add_3(num) for num in nums if num != 7]

return new_nums
```

</td>

<td>

```python
import functools
!import operator

def add(a, b):
    return a + b
add_3 = functools.partial(add, 3)

!ne_7 = functools.partial(operator.ne, 7)

nums = [4, 2, 7, 22]

!new_nums = [add_3(num) for num in nums if ne_7(num)]

return new_nums
```

</td>

</tr>

</table>

---

The list comprehension is a `filter` then a `map`.

<table width="100%">

<tr>
    <th width="50%">Before</th>
    <th width="50%">After</th>
</tr>

<tr>

<td>

```python
import functools
import operator

def add(a, b):
    return a + b
add_3 = functools.partial(add, 3)

ne_7 = functools.partial(operator.ne, 7)

nums = [4, 2, 7, 22]

new_nums = [add_3(num) for num in nums if ne_7(num)]

return new_nums
```

</td>

<td>

```python
import functools
import operator

def add(a, b):
    return a + b
add_3 = functools.partial(add, 3)

ne_7 = functools.partial(operator.ne, 7)

nums = [4, 2, 7, 22]

!nums_without_7 = filter(ne_7, nums)

!new_nums = map(add_3, nums_without_7)

return new_nums
```

</td>

</tr>

</table>

---

Explicit looping is gone, loops are "higher-order" concepts of `map`, `filter` (and `reduce`).

<table width="100%">

<tr>
    <th width="50%">Before</th>
    <th width="50%">After</th>
</tr>

<tr>

<td>

```python
def add(a, b):
    return a + b

nums = [4, 2, 7, 22]

new_nums = []

for num in nums:
    if num != 7:
        new_nums.append(add(3, num))

return new_nums
```

</td>

<td>

```python
import functools
import operator

def add(a, b):
    return a + b
add_3 = functools.partial(add, 3)

ne_7 = functools.partial(operator.ne, 7)
    
nums = [4, 2, 7, 22]

nums_without_7 = filter(ne_7, nums)

new_nums = map(add_3, nums_without_7)

return new_nums
```

</td>

</tr>

</table>

---

# COMMENTS

# QUESTIONS

# CONCERNS

---

Functional is better!

<br/>

<table width="100%">

<tr>
    <th width="50%">Elixir</th>
    <th width="50%">Racket</th>
</tr>

<tr>

<td>

```elixir
iex> nums = [4, 2, 7, 22]
[4, 2, 7, 22]

iex> nums
     |> Enum.filter(fn n -> n != 7 end)
     |> Enum.map(fn n -> n + 3 end)
[7, 5, 25]

# or, with the capture shorthand:
iex> nums
     |> Enum.filter(& &1 != 7)
     |> Enum.map(& &1 + 3)
[7, 5, 25]
```

</td><td>

```lisp
> (let [(nums '(4 2 7 22))
        (add-3 (curry + 3))
        (ne-7 (compose not (curry = 7)))]
    (map add-3 (filter ne-7 nums))
    )
'(7 5 25)

; absurd, or is it??!?
(let* [(nums '(4 2 7 22))
        (add-3 (curry + 3))
        (map-add-3 (curry map add-3))
        (ne-7 (compose not (curry = 7)))
        (filter-ne-7 (curry filter ne-7))
        (filter-ne-7-then-map-add-3 (compose map-add-3 filter-ne-7))]
    (filter-ne-7-then-map-add-3 nums)
    )
```

</td>

</tr>

</table>
