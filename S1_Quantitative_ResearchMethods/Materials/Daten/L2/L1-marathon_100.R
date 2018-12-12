
setwd("/Users/marianbuhler/go/src/mastering/S1_Quantitative_ResearchMethods/Materials/Daten/L1")
load("/Users/marianbuhler/go/src/mastering/S1_Quantitative_ResearchMethods/Materials/Daten/L1/marathon_100.RData")
with(marathon_100, Hist(hours, scale="frequency", breaks="Sturges", 
  col="darkgray"))
with(marathon_100, qqPlot(hours, dist="norm", id=list(method="y", n=2, 
  labels=rownames(marathon_100))))
library(abind, pos=17)
library(e1071, pos=18)
numSummary(marathon_100[,"hours", drop=FALSE], statistics=c("mean", "sd", 
  "IQR", "quantiles"), quantiles=c(0,.25,.5,.75,1))
normalityTest(~hours, test="shapiro.test", data=marathon_100)

