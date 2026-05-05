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

# What is Scrum?

#### Quentin Crain

https://scrumguides.org/scrum-guide.html

https://www.scrum.org/learning-series/what-is-scrum/

<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true, theme: 'default', securityLevel: 'loose', });
</script>

---

## Overview

<div style="display: inline-block; background: white; padding: 2px;">
<img src="scrum-framework-9.29.23.png">
</div>

---

## Roles

<!--
Value to Stakeholders
Value to Team
-->

<table>
    <tr>
        <th>Product Owner</th>
        <th>Scrum Master</th>
        <th>Developer</th>
    </tr>
    <tr>
        <td>
            <img src="scrum-product-owner-stances.png" width="225" />
            <img data-marpit-fragment src="Office-Space-Quotes-People-Skills.jpg" width="300" />
        </td>
        <td>
            <img src="scrum-scrummaster-stances.png" width="300" />
            <img data-marpit-fragment src="office-space-lumberg.jpg" width="300" />
        </td>
        <td>
            <img data-marpit-fragment src="office-space-developers.jpg" width="300" />
        </td>
    </tr>
</table>

---

## Artifacts

<table>
    <tr>
        <th>Product Backlog</th>
        <th>Sprint Backlog</th>
        <th>Work Item</th>
    </tr>
    <tr>
        <td>ordered list of what is needed to improve the product</td>
        <td>work committed by the developers to the PO in a timeframe</td>
        <td>work in the sprint</td>
    </tr>
</table>

---

## Ceremonies

<table>
    <tr>
        <th>Sprint Planning</th>
        <th>Daily Scrum</th>
        <th>Sprint Review</th>
        <th>Sprint Retrospective</th>
    </tr>
    <tr>
        <td>Build sprint backlog</td>
        <td>Review sprint progress</td>
        <td>Review work completed with Stakeholders</td>
        <td>Review sprint effectiveness and make change</td>
    </tr>
</table>

---

## Guidance

At the start of the sprint, you commit to the Customer to deliver items A, B, C of value.

At the Sprint Review, you demo to the Customer what you finished.

---

# E   N   D
