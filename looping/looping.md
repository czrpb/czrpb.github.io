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
- .

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

- Iteration
- Condition

---

## 2 Implementations of Looping

- Iteration
- Recursion

---

---

