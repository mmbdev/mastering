<!-- R Commander Markdown Template -->

L1 Marathon
=======================

### mmb

### 2018-12-12








```r
> load("C:/Users/mmb/go/src/mastering/S1_Quantitative_ResearchMethods/Materials/Daten/L2/marathon_1000.RData")
```



```r
> library(abind, pos=17)
```



```r
> library(e1071, pos=18)
```



```r
> numSummary(marathon_1000[,"age", drop=FALSE], statistics=c("mean", 
+   "quantiles"), quantiles=c(0,.25,.5,.75,1))
```

```
     mean 0% 25% 50% 75% 100%   n NA
 35.40302 17  28  34  42   67 995  5
```


```r
> setwd("C:/Users/mmb/go/src/mastering/S1_Quantitative_ResearchMethods/Materials/Daten/L2/Marathon1000")
```



