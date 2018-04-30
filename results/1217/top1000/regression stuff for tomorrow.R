run.regression(raw.data,
               predictor.columns.reduced,
               outcome.columns[1],
               scale.vars=TRUE)

run.regression(raw.data,
               remove.predictors(predictor.columns.full,
                                 c("AllPunc", "pronoun", "ppron", "affect", "function.", "relativ",
                                   "Dic", "cogproc", "Analytic", "informal", "social", "verb", "bio",
                                   "drives", "percept", "negemo", "Authentic", "auxverb", "Clout",
                                   "shehe", "differ", "prep", "AvgAuthor", "adverb", "Tone", "focuspresent",
                                   "OtherP", "conj", "adj")
               ),
               outcome.columns[1],
               scale.vars=TRUE,
               stepwise=TRUE)