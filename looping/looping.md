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

  ul li {
    font-size: 22pt;
  }

  ul li ul li {
    font-size: 18pt;
  }

  blockquote {
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

- Why Loop?
- What is a Loop?
- 2 Purposes for Looping
- 3 Implementations of Iteration
- 2 Implementations of Conditional

---

#### Click on <i class="fa-solid fa-person-running"></i> to run the code on Python Tutor

---

## Why Loop?

<img src="why_loop.png" width="600" />

<p>

**Because I need to do the same thing again!**

</p>

---

## What is a Loop?

<table width="100%" style="font-size: 22pt;">
<tr><td>

Find all the keys (files) in a directory

</td><td>

Check to see if my device has powered on

</td></tr>
</table>

**Are these the same?**

---

## It's All About Intent!

<img src="intent.png" width="600" />

---

## 2 Purposes for Looping

<img src="for_v_while.png" width="512" />

<table width="100%" style="font-size: 22pt;">

<tr><th>
Iteration
</th><th>
Condition
</th></tr>

<tr><td style="vertical-align: top;">

<div style="background: #2b2d33; text-align: left; font-family: Consolas; font-size: 14pt;">

for element in collection:
&nbsp;&nbsp;&nbsp;&nbsp;...

</div>

</td><td>

<div style="background: #2b2d33; text-align: left; font-family: Consolas; font-size: 14pt;">

while COND and collection:
&nbsp;&nbsp;&nbsp;&nbsp;...

</div>

</td></tr>
</table>

---

## 3 Implementations of Iteration

<img src="iteration.png" width="640" />

<table width="100%" style="font-size: 22pt;">

<tr><td style="vertical-align: top; width: 25%;">

<div class="code-container">

<a href="https://pythontutor.com/visualize.html#code=def%20process%28nums%29%3A%0A%20%20%20%20sum%20%3D%200%0A%20%20%20%20for%20num%20in%20nums%3A%0A%20%20%20%20%20%20%20%20sum%20%2B%3D%20num%0A%20%20%20%20return%20sum%0A%0Aresult%20%3D%20process%28%5B4%2C5%2C6%2C7%2C8%2C9%2C10%2C11%2C12%5D%29%0Aprint%28result%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false" class="run-icon" target="_blank"><i class="fa-solid fa-person-running"></i></a>

<div style="background: #2b2d33; text-align: left; font-family: Consolas; font-size: 10pt;">

def process(nums):
&nbsp;&nbsp;&nbsp;&nbsp;sum = 0
&nbsp;&nbsp;&nbsp;&nbsp;for num in nums:	
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sum += num
&nbsp;&nbsp;&nbsp;&nbsp;return sum

</div>

</div>

</td><td style="vertical-align: top;">

<div class="code-container">

<a href="https://pythontutor.com/visualize.html#code=def%20process%28nums%29%3A%0A%20%20%20%20if%20nums%3A%0A%20%20%20%20%20%20%20%20num%2C%20*nums%20%3D%20nums%0A%20%20%20%20%20%20%20%20return%20num%20%2B%20process%28nums%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%200%0A%0Aresult%20%3D%20process%28%5B4%2C5%2C6%2C7%2C8%2C9%2C10%2C11%2C12%5D%29%0Aprint%28result%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false" class="run-icon" target="_blank"><i class="fa-solid fa-person-running"></i></a>

<div style="background: #2b2d33; text-align: left; font-family: Consolas; font-size: 10pt;">

def process(nums):
&nbsp;&nbsp;&nbsp;&nbsp;if nums:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;num, *nums = nums
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return num + process(nums)
&nbsp;&nbsp;&nbsp;&nbsp;else:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return 0

</div>

</div>

</td><td style="vertical-align: top;">

<div class="code-container">

<a href="https://pythontutor.com/visualize.html#code=def%20process%28container%2C%20acc%3D0%29%3A%0A%20%20%20%20match%20container%3A%0A%20%20%20%20%20%20%20%20case%20%5B%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20acc%0A%20%20%20%20%20%20%20%20case%20%5Bnum%2C%20*nums%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20process%28nums%2C%20num%2Bacc%29%0A%0Aresult%20%3D%20process%28%5B4%2C5%2C6%2C7%2C8%2C9%2C10%2C11%2C12%5D%29%0Aprint%28result%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false" class="run-icon" target="_blank"><i class="fa-solid fa-person-running"></i></a>

<div style="background: #2b2d33; text-align: left; font-family: Consolas; font-size: 10pt;">

def process(container, acc=0):
&nbsp;&nbsp;&nbsp;&nbsp;match container:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;case []:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return acc
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;case [num, *nums]:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return process(nums, num+acc)

</div>

</div>

</td></tr>

</table>

---

## DONT!!!

<img src="bad_while_usage.png" width="768" />

---

### 2 Implementations of Conditional

<img src="conditional.png" width="400" />

<table width="100%" style="font-size: 12pt;">

<tr><td style="vertical-align: top; width: 45%;">

<div class="code-container">

<a href="https://pythontutor.com/visualize.html#code=def%20are_all_evens%28nums%29%3A%0A%20%20%20%20match%20nums%3A%0A%20%20%20%20%20%20%20%20case%20%5B%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20True%0A%20%20%20%20%20%20%20%20case%20%5Bnum,%20*nums%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%28num%20%25%202%20%3D%3D%200%29%20and%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20are_all_evens%28nums%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%0Aprint%28are_all_evens%28%5B2,4,6,8%5D%29%29%0Aprint%28are_all_evens%28%5B2,4,5,6,8%5D%29%29%0A&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false" class="run-icon" target="_blank"><i class="fa-solid fa-person-running"></i></a>

<div style="background: #2b2d33; text-align: left; font-family: Consolas; font-size: 15pt;">

def are_all_evens(nums):
&nbsp;&nbsp;&nbsp;&nbsp;even_so_far = True
&nbsp;&nbsp;&nbsp;&nbsp;while even_so_far and nums:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;num, *nums = nums
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;even_so_far &= num %2 == 0
&nbsp;&nbsp;&nbsp;&nbsp;return even_so_far

</div>

</div>

</td><td style="vertical-align: top;">

<div class="code-container">

<a href="https://pythontutor.com/visualize.html#code=def%20are_all_evens%28nums%29%3A%0A%20%20%20%20even_so_far%20%3D%20True%0A%20%20%20%20while%20even_so_far%20and%20nums%3A%0A%20%20%20%20%20%20%20%20num,%20*nums%20%3D%20nums%0A%20%20%20%20%20%20%20%20even_so_far%20%26%3D%20num%20%25%202%20%3D%3D%200%0A%20%20%20%20return%20even_so_far%0A%20%20%20%20%0Aprint%28are_all_evens%28%5B2,4,6,8%5D%29%29%0Aprint%28are_all_evens%28%5B2,4,5,6,8%5D%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false" class="run-icon" target="_blank"><i class="fa-solid fa-person-running"></i></a>

<div style="background: #2b2d33; text-align: left; font-family: Consolas; font-size:15pt;">

def are_all_evens(nums):
&nbsp;&nbsp;&nbsp;&nbsp;match nums:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;case []:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return True
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;case [num, *&lowbar;] if num % 2 != 0:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return False
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;case [&lowbar;, *nums]:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return are_all_evens(nums)

</div>

</div>

</td></tr>

</table>

---

## DONT!!!

<img src="bad_for_usage.png" width="768" />

---

<p align="left">Use <tt>for</tt> when:</p>

> You are operating on a collection or iterable. You should be acting on each item. You are done when you have acted on the whole list.

<br/>

<p align="left">Use <tt>while</tt> when:</p>

> You are checking a condition or state. You should be acting while the condition is unchanged. You are done when the condition changes.

<br/>

<a style="font-size: 20pt;" href="claude-report-from-discussion.pdf">Claude's Report of Our Conversation</a>

---

# E N D
