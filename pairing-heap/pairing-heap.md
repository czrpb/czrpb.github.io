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
    font-size: 16pt;
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

# Pairing Heap

## What is a heap?

Quentin Crain

<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true, theme: 'default', securityLevel: 'loose', });
</script>

---

## Agenda

- Heap
  - Definition
  - Purpose
  - .

- Pairing Heap
  - Definition
  - Purpose
  - Structure
  - Behaviors
  - .

- Bonus / Random
  - How was this presentation created? **[MARP](https://marp.app/)**
  - <span class="fa-solid fa-brain"> More Education!</span>
  - <span class="fa-solid fa-laptop-code"> Practical Learning!</span>

---

### Heap: Definition

<span style="font-size: 18pt;">
A heap is a tree-like structure where the root node meets some criteria, such as minimum or maximum value.
</span>

<table width="100%" style="font-size: 22pt;">
<tr><td width="50%" style="vertical-align: top;">

<p class="fa-solid fa-brain my-medium-size">
<a href="https://en.wikipedia.org/wiki/Tree_(abstract_data_type)">Tree</a>
</p>

<div style="display: flex; align-items: center; justify-content: center;">

<div class="mermaid" style="background: white;">
graph TD
    root["B2"]
    root --> A["A"]
    root --> B["B"]
    root --> C1["C1"]
    root --> D["D"]
    B --> B1["B1"]
    C1 --> C["C"]
    C1 --> C2["C2"]
    classDef box fill:#f5f5f0,stroke:#000000,stroke-width:2px,color:#000000;
    class root,A,B,C,D,B1,C1,C2 box;
</div>

</div>

</td><td style="vertical-align: top;">

<p class="fa-solid fa-brain my-medium-size">
<a href="https://en.wikipedia.org/wiki/Heap_(data_structure)">Heap</a>
</p>

<div style="display: flex; align-items: center; justify-content: center;">

<div class="mermaid" style="background: white;">
graph TD
    A["A"]
    A --> B2["B2"]
    A --> C["C"]
    A --> B1["B1"]
    A --> B["B"]
    B2 --> C1["C1"]
    C --> C2["C2"]
    C2 --> D["D"]
    classDef box fill:#f5f5f0,stroke:#000000,stroke-width:2px,color:#000000;
    class B2,A,B,C,D,B1,C1,C2 box;
</div>

</div>

</td></tr>
</table>

---

asdf

---
