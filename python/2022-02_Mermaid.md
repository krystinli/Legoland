# Mermaid 🧜‍♀️
On Feb 14, 2022, Mermaid finally made its way to Github MD 👏
- [x] [Basic Flowchart]((https://mermaid-js.github.io/mermaid/#/./flowchart?id=flowcharts-basic-syntax))
- [ ] [Subgraph](https://mermaid-js.github.io/mermaid/#/./flowchart?id=subgraphs)

## 01_Flowchart
All Flowcharts are composed of 
1. Nodes
2. The geometric shapes
3. Edges: the arrows or lines

**A node:** The id is what is displayed in the box.
```
graph LR;
    id1[This is the text in the box]
```

```mermaid
graph LR;
    id1[This is the text in the box]
```

**A graph:** This statement declares the direction of the Flowchart.
- TD: This declares the flowchart is oriented from top to bottom (TD or TB)
- LR: This declares the flowchart is oriented from left to right

```
graph TD;
    A-->B;
    A-->C;
```

```mermaid
graph TD;
    A-->B;
    A-->C;
```

```
flowchart LR;
    Start-->Finish;
```

```mermaid
flowchart LR;
    Start-->Finish;
```

### More
- Nodes shapes [[here]](https://mermaid-js.github.io/mermaid/#/./flowchart?id=node-shapes)
- Link betwee nodes [[here]](https://mermaid-js.github.io/mermaid/#/./flowchart?id=links-between-nodes)
