# Mermaid Family Tree Diagram Template

This folder contains templates for creating family tree visualizations using Mermaid diagrams.

## Basic Family Tree Diagram

This template shows a simple family tree with two parents and their children.

```mermaid
graph TD
    A[Parent One] --> B[Child One]
    A --> C[Child Two]
    A --> D[Child Three]
    
    E[Parent Two] --> B
    E --> C
    E --> D
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style E fill:#bbf,stroke:#333,stroke-width:2px
```

## Enhanced Family Tree with Lifespans

This template shows a family tree with birth and death dates.

```mermaid
graph TD
    A[Name One<br/>1890-1965] --> B[Name Two<br/>1910-1980]
    A --> C[Name Three<br/>1915-1990]
    A --> D[Name Four<br/>1920-2000]
    
    E[Name Five<br/>1895-1970] --> B
    E --> C
    E --> D
    
    F[Name Six<br/>1930-2010] --> G[Name Seven<br/>1950-]
    F --> H[Name Eight<br/>1955-]
    
    B --> I[Name Nine<br/>1940-2015]
    C --> J[Name Ten<br/>1945-]
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style E fill:#bbf,stroke:#333,stroke-width:2px
    style F fill:#bfb,stroke:#333,stroke-width:2px
    style I fill:#ffb,stroke:#333,stroke-width:2px
```

## Timeline Visualization

This template shows a family timeline using a Gantt chart.

```mermaid
gantt
    title Family Timeline
    dateFormat YYYY
    
    section First Generation
    Grandparent One       :active, gen1, 1890, 1965
    Grandparent Two       :active, gen2, 1895, 1970
    
    section Second Generation
    Parent One            :active, gen3, 1910, 1980
    Parent Two            :active, gen4, 1915, 1990
    
    section Third Generation
    Child One             :active, gen5, 1940, 2015
    Child Two             :crit, gen6, 1945, -
    Child Three           :active, gen7, 1950, -
```

## Relationship Map

This template shows a more complex relationship map.

```mermaid
graph LR
    A[Grandparent One] --> B[Parent One]
    A --> C[Aunt/Uncle One]
    
    D[Grandparent Two] --> B
    D --> C
    
    B --> E[You]
    B --> F[Sibling One]
    
    G[Spouse's Parent One] --> H[Spouse]
    I[Spouse's Parent Two] --> H
    
    H --> J[Child One]
    H --> K[Child Two]
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style D fill:#bbf,stroke:#333,stroke-width:2px
    style G fill:#bfb,stroke:#333,stroke-width:2px
    style I fill:#ffb,stroke:#333,stroke-width:2px
```

## Historical Context

This template shows a family tree with historical events.

```mermaid
gantt
    title Family Timeline with Historical Context
    dateFormat YYYY
    
    section Family Events
    Grandparent One       :active, gen1, 1890, 1965
    World War I           :milestone, wwi, 1914, 1918
    Parent One            :active, gen2, 1910, 1980
    World War II          :milestone, wwii, 1939, 1945
    Child One             :active, gen3, 1940, 2015
    Cold War              :phase, coldwar, 1947, 1991
    Child Two             :active, gen4, 1950, -
    9/11                  :milestone, 911, 2001, 2001
    Child Three           :active, gen5, 1955, -
    
    section Historical Events
    Spanish Flu           :active, flu, 1918, 1920
    Great Depression      :phase, depression, 1929, 1939
    Vietnam War           :active, vietnam, 1955, 1975
    Internet Age          :phase, internet, 1990, -
```

## Customization

You can customize these templates by:

1. Changing colors using the `style` directive
2. Adding more people or events
3. Adjusting the layout using different Mermaid graph types
4. Including images or links to more detailed information

For more advanced visualizations, consider using D3.js examples in the `d3` folder.
