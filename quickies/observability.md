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

# Observability

### Quentin Crain

https://opentelemetry.io/docs/concepts/observability-primer/

<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true, theme: 'default', securityLevel: 'loose', });
</script>

---

> Observability is the property of a software system that lets you infer its internal state from the outputs it already emits, without shipping new code or attaching a debugger. The term is borrowed from control theory and adapted loosely: a system is observable to the degree that it can answer questions you didn't know to ask in advance. This is what distinguishes it from monitoring, which checks predefined conditions and handles known failure modes well but struggles with the emergent, cross-service problems typical of distributed systems. The conventional account organises observability around three pillars — logs, metrics, and traces — though a sharper view treats these as projections of a single underlying stream of wide, high-cardinality structured events. OpenTelemetry has become the de facto standard for vendor-neutral instrumentation. Two caveats matter: the term is heavily marketed and often conflated with traditional monitoring tooling, and observability supplies evidence about system behaviour but not understanding of it — that still depends on the team's theory of the system.

---

# E N D
