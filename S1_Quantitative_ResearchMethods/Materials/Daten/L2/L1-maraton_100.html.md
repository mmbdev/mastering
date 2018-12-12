<!-- R Commander Markdown Template -->

VL Normal Distribution marathon_100 hours
=======================

### mmb

### `r as.character(Sys.Date())`

```{r echo=FALSE}
# include this code chunk as-is to set options
knitr::opts_chunk$set(comment=NA, prompt=TRUE, out.width=750, fig.height=8, fig.width=8)
library(Rcmdr)
library(car)
library(RcmdrMisc)
```


```{r echo=FALSE}
# include this code chunk as-is to enable 3D graphs
library(rgl)
knitr::knit_hooks$set(webgl = hook_webgl)
```

### Working Directory setzten

```{r}
setwd("/Users/marianbuhler/go/src/mastering/S1_Quantitative_ResearchMethods/Materials/Daten/L1")
```

### Daten laden

```{r}
load("/Users/marianbuhler/go/src/mastering/S1_Quantitative_ResearchMethods/Materials/Daten/L1/marathon_100.RData")
```

## Histo Var hours

```{r}
with(marathon_100, Hist(hours, scale="frequency", breaks="Sturges", 
  col="darkgray"))
```

## QQ-Plott hours


```{r}
with(marathon_100, qqPlot(hours, dist="norm", id=list(method="y", n=2, 
  labels=rownames(marathon_100))))
```

### Interpretation: Datenpunkte sind innerhalb des Konfidenzbereiches, deutet auf Normalverteilung hin N(0,1)

## Exzess Kurtosis und Schiefe


```{r}
library(abind, pos=17)
```


```{r}
library(e1071, pos=18)
```


```{r}
numSummary(marathon_100[,"hours", drop=FALSE], statistics=c("mean", "sd", 
  "IQR", "quantiles"), quantiles=c(0,.25,.5,.75,1))
```

## Interpretation: Weicht etwas von Normalverteilung ab. 

### Shapiro-Wilk-Test

```{r}
normalityTest(~hours, test="shapiro.test", data=marathon_100)
```

##Interpretation: Wahrscheinlichkeit, dass H0 korrekt ist, ist deutlich gr<c3><b6><c3><9f>er als 0.05 (p-Value ist gleich 0.2334).


# Schlussfolgerung

Verfahren deuten darauf hin, dass die Variable in Ihrer Grundgesamtheit normalverteilt ist.


