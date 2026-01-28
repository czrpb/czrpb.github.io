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

<tr><td>

```python
sum = 0
for num in nums:
    sum += num
```

<a href="https://pythontutor.com/visualize.html#code=acc%20%3D%200%0Anums%20%3D%20range%284%2C13%29%0Afor%20num%20in%20nums%3A%0A%20%20%20%20acc%20%2B%3D%20num%0Aprint%28acc%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false">Python Tutor</a>

</td><td>

```python
def process(nums):
    if nums:
        num, *nums = nums
        return num + process(nums)
    else:
        return 0
```

</td><td>

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

## 2 Implementations of Conditional


---

