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
    font-size: 13pt;
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

  ul li ul li {
    font-size: 22pt;
  }

  footer {
    left: auto;
    right: auto;
    top: auto;
    bottom: auto;

    right: 20px;
    top: 20px;
  }

  tr td {
    position: relative;
  }
  
  .run-icon {
    position: absolute;
    top: 1.4em;
    right: 1em;
    color: white;
    font-size: 0.5em;
    text-decoration: none;
    z-index: 10;
    transition: color 0.2s ease;
  }

  .run-icon:hover {
    color: lightgreen;
  }

---

# Looping

## That's easy!

Quentin Crain

<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true });
</script>

---

## Agenda

- What / Why Loop?
- 2 Purposes for Looping
- 3 Implementations of Iteration
- 2 Implementations of Conditional

---

## What / Why Loop?

<table width="100%" style="font-size: 22pt;">
<tr><td colspan="2">

Because I need to do (nearly) the same thing again!

</td></tr><tr><td>

Find all the keys (files) in a directory

</td><td>

Check to see if my device has powered on

</td></tr>
</table>

Are these the same?

---

## 2 Purposes for Looping

<img src="for_v_while.png" width="512" />


<table width="100%" style="font-size: 22pt;">

<tr><th>
Iteration
</th><th>
Condition
</th></tr>

<tr><td>

```python
for element in container:
    f(element)
```

</td><td>

```python
element, *container = container
while cond(element):
    element, *container = container
```

</td></tr>
</table>

---

## 3 Implementations of Iteration

<img src="iteration.png" width="640" />

<table width="100%" style="font-size: 22pt;">

<tr><td style="vertical-align: top;">

<a href="https://pythontutor.com/visualize.html#code=def%20process%28nums%29%3A%0A%20%20%20%20sum%20%3D%200%0A%20%20%20%20for%20num%20in%20nums%3A%0A%20%20%20%20%20%20%20%20sum%20%2B%3D%20num%0A%20%20%20%20return%20sum%0A%0Aresult%20%3D%20process%28%5B4%2C5%2C6%2C7%2C8%2C9%2C10%2C11%2C12%5D%29%0Aprint%28result%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false" class="run-icon" target="_blank"><i class="fa-solid fa-person-running"></i></a>

```python
def process(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum
```

</td><td style="vertical-align: top;">

<a href="https://pythontutor.com/visualize.html#code=def%20process%28nums%29%3A%0A%20%20%20%20if%20nums%3A%0A%20%20%20%20%20%20%20%20num%2C%20*nums%20%3D%20nums%0A%20%20%20%20%20%20%20%20return%20num%20%2B%20process%28nums%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%200%0A%0Aresult%20%3D%20process%28%5B4%2C5%2C6%2C7%2C8%2C9%2C10%2C11%2C12%5D%29%0Aprint%28result%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false" class="run-icon" target="_blank"><i class="fa-solid fa-person-running"></i></a>

```python
def process(nums):
    if nums:
        num, *nums = nums
        return num + process(nums)
    else:
        return 0
```

</td><td style="vertical-align: top;">

<a href="https://pythontutor.com/visualize.html#code=def%20process%28container%2C%20acc%3D0%29%3A%0A%20%20%20%20match%20container%3A%0A%20%20%20%20%20%20%20%20case%20%5B%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20acc%0A%20%20%20%20%20%20%20%20case%20%5Bnum%2C%20*nums%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20process%28nums%2C%20num%2Bacc%29%0A%0Aresult%20%3D%20process%28%5B4%2C5%2C6%2C7%2C8%2C9%2C10%2C11%2C12%5D%29%0Aprint%28result%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false" class="run-icon" target="_blank"><i class="fa-solid fa-person-running"></i></a>

```python
def process(container, acc=0):
    match container:
        case []:
            return acc
        case [num, *nums]:
            return process(nums, num+acc)
```

</td></tr>

</table>

---

### 2 Implementations of Conditional

<img src="conditional.png" width="400" />

<table width="100%" style="font-size: 12pt;">

<tr><td style="vertical-align: top;">

```python
def first_sqrt(nums):
    num = None
    while (
        nums
        and not math.sqrt(num := nums[0]).is_integer()
    ):
        nums = nums[1:]
    return num
```


</td><td style="vertical-align: top;">

```python
def first_sqrt(nums):
    if not nums:
        return None
    num, *nums = nums
    if math.sqrt(num).is_integer():
        return num
    else:
        return first_sqrt(nums)
```

</td></tr>
<tr><td style="vertical-align: top;">

```python
next(
    (num
     for num in nums
     if math.sqrt(num).is_integer()
    ),
    None
)
```

</td><td style="vertical-align: top;">

```python
def first_sqrt(nums):
    match nums:
        case []:
            return None
        case [num, *_] if math.sqrt(num).is_integer():
            return num
        case [_, *nums]:
            return first_sqrt(nums)
```

</td></tr>

</table>

---

## DONT!!!

<img src="bad_for_usage.png" width="768" />

---

# E N D
