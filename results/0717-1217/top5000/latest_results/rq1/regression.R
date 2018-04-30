library(car)
library(igraph)
library(pls)
library(MASS)
library(broom)
library(corrplot)

set.seed(2017) # just any number to "fix" random number generator so each run produces the same results


#setwd("~/Desktop/0517/")

raw.y <- read.csv("centrality.csv")
raw.x <- read.csv("features.csv")
raw.data <- merge(raw.x, raw.y, by.x = "subreddit", by.y = "subreddit")
raw.data$Segment<-NULL
raw.data$X.1<-NULL
raw.data$X.x<-NULL
raw.data$X.y<-NULL


predictor.columns.full <- colnames(raw.data)[2:96]
predictor.columns.reduced <- colnames(raw.data)[2:11]

outcome.columns <- colnames(raw.data)[97:100]

run.regression <- function(regression.data, predictor.columns, outcome.var, scale.vars=TRUE, stepwise=F) {
  formula.data <- regression.data

  if(scale.vars) {
    print("scaling predictors")
    formula.data[,predictor.columns] <- scale(regression.data[,predictor.columns])
    formula.data[, outcome.var] <- scale(formula.data[, outcome.var])
  }

  regression.formula.str <- paste(outcome.var, " ~ ", paste(predictor.columns, collapse=" + "))
  print("processing regression formula:")
  print(regression.formula.str)

  lm.model <- lm(as.formula(regression.formula.str), data=formula.data)

  print(summary(lm.model))
  vifs <- round(vif(lm.model),2)
  print("Printing VIFS now: ")
  print(vifs[order(vifs)])

  if(stepwise) {
    reduced.model <- stepAIC(lm.model, direction="both")

    print(summary(reduced.model))
    vifs <- round(vif(reduced.model),2)
    print(vifs[order(vifs)])
  }
}

remove.predictors <- function(predictors, remove.predictors) {
  predictors[predictors %in% remove.predictors==F]
}

sink('betweenness_stepwise.txt')
run.regression(raw.data,
               remove.predictors(predictor.columns.full,
                                 c("AllPunc", "ppron", "pronoun", "affect", "function.", "informal", "Dic", "Analytic", "cogproc", "relativ", "social", "bio", "verb", "percept", "negemo", "drives", "shehe", "AvgAuthor", "Authentic", "focuspresent", "Clout", "posemo", "auxverb", "prep")
               ),
               outcome.columns[1],
               scale.vars=TRUE,
               stepwise=TRUE)
sink()

sink('closeness_stepwise.txt')
run.regression(raw.data,
               remove.predictors(predictor.columns.full,
                                 c("AllPunc", "ppron", "pronoun", "affect", "function.", "informal", "Dic", "Analytic", "cogproc", "relativ", "social", "bio", "verb", "percept", "negemo", "drives", "shehe", "AvgAuthor", "Authentic", "focuspresent", "Clout", "posemo", "auxverb", "prep")
               ),
               outcome.columns[2],
               scale.vars=TRUE,
               stepwise=TRUE)
sink()

sink('eigen_centrality_stepwise.txt')
run.regression(raw.data,
               remove.predictors(predictor.columns.full,
                                 c("AllPunc", "ppron", "pronoun", "affect", "function.", "informal", "Dic", "Analytic", "cogproc", "relativ", "social", "bio", "verb", "percept", "negemo", "drives", "shehe", "AvgAuthor", "Authentic", "focuspresent", "Clout", "posemo", "auxverb", "prep")
               ),
               outcome.columns[3],
               scale.vars=TRUE,
               stepwise=TRUE)
sink()

sink('degree_stepwise.txt')
run.regression(raw.data,
               remove.predictors(predictor.columns.full,
                                 c("AllPunc", "ppron", "pronoun", "affect", "function.", "informal", "Dic", "Analytic", "cogproc", "relativ", "social", "bio", "verb", "percept", "negemo", "drives", "shehe", "AvgAuthor", "Authentic", "focuspresent", "Clout", "posemo", "auxverb", "prep")
               ),
               outcome.columns[4],
               scale.vars=TRUE,
               stepwise=TRUE)
sink()