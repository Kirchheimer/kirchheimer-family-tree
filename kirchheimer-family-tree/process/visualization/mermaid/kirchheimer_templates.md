# Kirchheimer Family Tree Mermaid Templates

This folder contains Mermaid templates specifically designed for visualizing the Kirchheimer family tree data.

## Main Kirchheimer Lineage

This template shows the main Kirchheimer lineage from the 18th century to the present day.

```mermaid
graph TD
    A[Wolf Loew<br/>c.1695-~1795<br/>First Kirchheimer ancestor] --> B[Nathan Levi Wolf<br/>~1729-~1795]
    A --> C[Sara]
    
    B --> D[Samson Nathan Kirchheimer<br/>1772-1855]
    B --> E[Bluem Loew<br/>1773-1845]
    
    D --> F[Nathan Kirchheimer<br/>1799-1862<br/>Married Susan Hanauer]
    E --> G[Susan Hanauer<br/>1802-1867<br/>Maternal line from Hanauer family]
    
    F --> H[Moses Kirchheimer<br/>1835-1893<br/>Born in Berwangen]
    F --> I[Samson Kirchheimer<br/>1872-1941<br/>Immigrated to US]
    
    H --> J[Samson Kirchheimer<br/>1872-1941<br/>Texas businessman]
    H --> K[Babette Westheimer<br/>1838-1907<br/>Maternal line from Westheimer family]
    
    J --> L[Joseph Kirchheimer<br/>1916-1970<br/>Attorney]
    J --> M[Nathan Kirchheimer<br/>1896-1934]
    J --> N[Thora Kirchheimer<br/>~1910-?]
    J --> O[Borghild Kirchheimer<br/>1914-1986]
    J --> P[Theodore R. Kirchheimer<br/>1918-2009]
    
    style A fill:#ffb,stroke:#333,stroke-width:2px
    style D fill:#ffb,stroke:#333,stroke-width:2px
    style I fill:#ffb,stroke:#333,stroke-width:2px
    style J fill:#f9f,stroke:#333,stroke-width:2px
    style L fill:#f9f,stroke:#333,stroke-width:2px
```

## Kirchheimer in America

This template focuses on the American branch of the Kirchheimer family.

```mermaid
graph TD
    A[Samson Kirchheimer<br/>1872-1941<br/>Immigrated 1889] --> B[Joseph Kirchheimer<br/>1916-1970<br/>Attorney, Houston]
    A --> C[Nathan Kirchheimer<br/>1896-1934<br/>Grocer, Houston]
    A --> D[Thora Kirchheimer<br/>~1910-?]
    A --> E[Borghild Kirchheimer<br/>1914-1986]
    A --> F[Theodore R. Kirchheimer<br/>1918-2009<br/>Attorney, Houston]
    
    B --> G[Joseph's children<br/>and descendants]
    C --> H[Nathan's children<br/>and descendants]
    D --> I[Thora's children<br/>and descendants]
    E --> J[Borghild's children<br/>and descendants]
    F --> K[Theodore's children<br/>and descendants]
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#f9f,stroke:#333,stroke-width:2px
    style F fill:#f9f,stroke:#333,stroke-width:2px
```

## Hanauer Lineage

This template shows the Hanauer maternal lineage which connects to the Kirchheimer family.

```mermaid
graph TD
    A[Naftali Herz Hanauer<br/>~1695-~1795<br/>From Hanau, Germany] --> B[Gerson Herz Hanauer<br/>~1751-1839]
    A --> C[Sophie Kahn]
    
    B --> D[Moses Herz Hanauer<br/>~1760-1823<br/>Cantor in Richen]
    B --> E[Jacob Hanauer<br/>1768-1832<br/>Merchant]
    
    D --> F[Susan Hanauer<br/>1802-1867<br/>Married Nathan Kirchheimer]
    E --> G[Descendants]
    
    F --> H[Nathan Kirchheimer<br/>1799-1862]
    
    style D fill:#bbf,stroke:#333,stroke-width:2px
    style F fill:#bbf,stroke:#333,stroke-width:2px
```

## Westheimer Lineage

This template shows the Westheimer maternal lineage which also connects to the Kirchheimer family.

```mermaid
graph TD
    A[Joseph Aron Westheimer<br/>~1765-1849<br/>Menzingen, Baden] --> B[Isaac Westheimer<br/>~1800-?]
    A --> C[Magdalena]
    
    B --> D[Isaak Westheimer<br/>c.1800<br/>Married Guedel Kaufmann]
    B --> E[Guedel Kaufmann<br/>c.1805<br/>From Menzingen]
    
    D --> F[Babette Westheimer<br/>1838-1907<br/>Married Moses Kirchheimer]
    
    F --> G[Moses Kirchheimer<br/>1835-1893<br/>Born in Berwangen]
    
    style F fill:#bfb,stroke:#333,stroke-width:2px
    style G fill:#bfb,stroke:#333,stroke-width:2px
```

## Timeline of Kirchheimer Family

This template shows a timeline of key events in the Kirchheimer family history.

```mermaid
gantt
    title Kirchheimer Family Timeline
    dateFormat YYYY
    
    section German Period
    Wolf Loew lineage      :c1, 1700, 1800
    Kirchheimer name adoption :milestone, 1809, 1809
    Napoleonic Wars        :phase1, 1803, 1815
    Political upheavals    :phase2, 1830, 1850
    Emancipation laws      :milestone, 1862, 1862
    
    section Immigration Period
    First emigration wave   :phase3, 1880, 1910
    Second emigration wave  :phase4, 1933, 1940
    
    section American Period
    Business ventures      :phase5, 1920, 1950
    Second generation      :phase6, 1950, 2000
    Modern descendants     :phase7, 2000, 2025
```

## Historical Context

This template shows the Kirchheimer family timeline with important historical events.

```mermaid
gantt
    title Kirchheimer Family in Historical Context
    dateFormat YYYY
    
    section Family Events
    Wolf Loew in Germany   :active, wolf, 1720, 1800
    Kirchheimer name       :milestone, name, 1809, 1809
    Emancipation           :milestone, emanc, 1862, 1862
    Immigration to US      :active, imm, 1880, 1920
    Holocaust              :active, holocaust, 1933, 1945
    American success       :active, success, 1950, 2000
    
    section Historical Events
    Seven Years' War       :active, war1, 1756, 1763
    French Revolution      :milestone, fr, 1789, 1799
    Napoleonic Wars        :active, nap, 1803, 1815
    1848 Revolutions       :milestone, 1848, 1848
    German Unification     :milestone, germ, 1871, 1871
    World War I            :active, wwi, 1914, 1918
    Great Depression       :phase, gd, 1929, 1939
    World War II           :active, wwii, 1939, 1945
    Cold War               :phase, cw, 1947, 1991
