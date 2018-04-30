sink('betweenness_all.txt')
run.regression(raw.data,
               predictor.columns.full,
               outcome.columns[1],
               scale.vars=TRUE)
sink()

sink('closeness_all.txt')
run.regression(raw.data,
               predictor.columns.full,
               outcome.columns[2],
               scale.vars=TRUE)
sink()

sink('eigen_centrality_all.txt')
run.regression(raw.data,
               predictor.columns.full,
               outcome.columns[3],
               scale.vars=TRUE)
sink()

sink('degree_all.txt')
run.regression(raw.data,
               predictor.columns.full,
               outcome.columns[4],
               scale.vars=TRUE)
sink()

sink('betweenness_stepwise.txt')
run.regression(raw.data,
               remove.predictors(predictor.columns.full,
                                 c("ScoreOver200Count", "ScoreOver1000Count", "AvgScorePerDay", "ScoreOver100Count", "ScoreOver500Count", "AvgGildedPostsPerDay", "AvgAuthor", "AvgPost", "AvgGoldPerDay")
               ),
               outcome.columns[1],
               scale.vars=TRUE,
               stepwise=TRUE)
sink()

sink('closeness_stepwise.txt')
run.regression(raw.data,
               remove.predictors(predictor.columns.full,
                                 c("ScoreOver200Count", "ScoreOver1000Count", "AvgScorePerDay", "ScoreOver100Count", "ScoreOver500Count", "AvgGildedPostsPerDay", "AvgAuthor", "AvgPost", "AvgGoldPerDay")
               ),
               outcome.columns[2],
               scale.vars=TRUE,
               stepwise=TRUE)
sink()

sink('eigen_centrality_stepwise.txt')
run.regression(raw.data,
               remove.predictors(predictor.columns.full,
                                 c("ScoreOver200Count", "ScoreOver1000Count", "AvgScorePerDay", "ScoreOver100Count", "ScoreOver500Count", "AvgGildedPostsPerDay", "AvgAuthor", "AvgPost", "AvgGoldPerDay")
               ),
               outcome.columns[3],
               scale.vars=TRUE,
               stepwise=TRUE)
sink()

sink('degree_stepwise.txt')
run.regression(raw.data,
               remove.predictors(predictor.columns.full,
                                 c("ScoreOver200Count", "ScoreOver1000Count", "AvgScorePerDay", "ScoreOver100Count", "ScoreOver500Count", "AvgGildedPostsPerDay", "AvgAuthor", "AvgPost", "AvgGoldPerDay")
               ),
               outcome.columns[4],
               scale.vars=TRUE,
               stepwise=TRUE)
sink()