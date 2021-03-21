# NBA Data Analysis

.... Pranav

### Results of games

Each game in a season of NBA is associated with many stats. These stats range from the number of points scored by each team in the game, to the percentage of baskets that were a result of a player's assist. These statistics can be used to help a machine learning program *learn* how a particular team will perform against another team.

Performing web scraping using Python libraries like Selenium and BeautifulSoup on popular basketball statistics websites like [Basketball-Reference.com](https://www.basketball-reference.com/) and the official [NBA Stats Website](https://www.nba.com/stats/), we were able to extract the month-wise stats for each team that played a game in the regular NBA Season of 2018-19. After combining the month-wise stats with each game that was played in the season, we were able to obtain an extensive dataset which contained team-wise stats for every game in the season. On performing Exploratory Data Analysis, we were able to find highly correlated features which would have an undesired effect on the learning of the machine learning model. The following heatmap shows the correlation coefficients of some of the input features:

![heatmap-image](/assets/report_images/heatmap.png)

After preprocessing the data and fitting the model on the preprocessed data using several different machine learning model architectures, we were able to obtain a model that was able to successfully predict the outcome of NBA games with **~73% accuracy**.

![training-img](/assets/report_images/train.png)

### Box Score

In basketball, box scores provide detailed statistics about each **player** who is on the lineup for a game. Additionally, it contains some team-level information like the 5 players who started the game, team rebounds, etc.
These box scores provide valuable insights on the skills of each player, and allows a machine learning model to learn certain performance metrics about each player and predict a player's performance in a simulated scenario.

Keshav Puranmalka proposes in his [paper](https://dspace.mit.edu/bitstream/handle/1721.1/85464/870969496-MIT.pdf) to create novel features in order to more accurately predict the skills of a player. Box scores only provide advanced statistics for plays that occur on the basketball court, during the game. However, other features which might not be related to the actual basketball game may be of importance to predict a player's (and the whole team's) performance. Some examples may include the number of rest days between two games, the geographical distance travelled by the team between two games, etc. *"Clutch"* moments in a game (game situations which are more important than others) are also a major consideration when evaluating a player's performance at a particular time in the game.

Using feature selection algorithms and Support Vector Machines (SVM) to predict the performance of team-level and player-level performances, the results prove to be **~2-3% more accurate** than publicly available state-of-the-art predictors of NBA game outcomes.


### Synergy

... Sanjkeet

### Positive and Negative Synergies

**About the paper**

Allan Z. Maymin et al.[4] provide a novel Skills Plus Minus (“SPM”) framework that can be used to measure synergies within basketball lineups, provide roster-dependent rankings of free agents, and generate mutually beneficial trades.

An evaluation on each player’s offense and defense in the SPM framework for three basic skill categories is done:

1. **Ball-handling Category**: Steal, Non-steal turnover
2. **Rebounding Category**: Rebound of a missed field goal, Rebound of a missed free throw
3. **Scoring Category**: Made field goal (2 or 3 points),

The synergies of each NBA team is calculated by comparing their 5-player lineup’s effectiveness to the “sum-of-the-parts.” The framework generates mutually beneficial trades between teams. Because skills have different synergies with other skills, the framework predicts that a player’s value depends on the other nine players on the court.

While these box score ratings can measure an individual’s contributions, they do not
necessarily explain how players interact on the court. For example, it is possible that the five
best players in the NBA are all centers. In this case, a team with five centers may not be the
optimal lineup, since there would be no one to bring the ball up the court or guard the quicker
opposing guards.

Certain trades can also be predicted using the framework.
It predicted that in the 2009-10 season, if the New Orleans Hornets traded Chris Paul for Deron Williams from the Utah Jazz, both the teams would have been a mutually beneficial trade.

The Probabilty of an event to occur is calculated using the below formula

![Conditional probability of each event](https://github.com/harsh2338/nba-prediction/blob/main/assets/report_images/conditional_probability.png)

For example, the probabilty of a steal by Rondo is given as:

![Example of probability of a steal](https://github.com/harsh2338/nba-prediction/blob/main/assets/report_images/example_prob_of_steal.png)

Using the probabilities the series of events can be predicted using the flow diagram

![Flow of events](https://github.com/harsh2338/nba-prediction/blob/main/assets/report_images/events_flow.png)

**Individual Player Ratings**:
By this example we can explain how a player is rated. Let’s say we create a fictional player who has Ronnie Brewer’s “steals” ratings, but is replacement level in all other skills. We then simulate games where one team consists of the fictional player and four replacement players, and their opponent utilizes five replacement players. The estimated point differential of this game is the player’s ratings for that particular skill.

Synergies are measured by how many additional points a combination of two skills create. For
example, Chris Paul's offensive ballhandling is worth 4.8 points, while Reggie Evans' offensive
rebounding is worth 3.1 points. We calculate that a team with Chris Paul's offensive
ballhandling and Reggie Evans’ defensive rebounding will have a 8.1 point advantage.
Therefore we calculate synergies as worth 0.2 points (8.1-4.8-3.1). Synergies are the difference
between the point differential of the combined team and the sum of the two individual players;
they tell us which types of players work well with one another.

For constructing a team, a few star players are chosen for a team and all the other players are made as free agents. By generating multiple combinations, a team can be completed by calculating the maximum team rating.

### Generating Line ups

...

Light Sanjkeet, Harsh

**LightGBM**

Gradient boosting refers to a class of ensemble machine learning algorithms that can be used for classification or regression predictive modeling problems.

Ensembles are constructed from decision tree models. Trees are added one at a time to the ensemble and fit to correct the prediction errors made by prior models. This is a type of ensemble machine learning model referred to as boosting.

Models are fit using any arbitrary differentiable loss function and gradient descent optimization algorithm. This gives the technique its name, “gradient boosting,” as the loss gradient is minimized as the model is fit, much like a neural network.

LightGBM is a gradient boosting framework that uses a tree based learning algorithm. It extends the gradient boosting algorithm by adding a type of automatic feature selection as well as focusing on boosting examples with larger gradients. It is widely used in cases of tabular data for regression and classification.

LightGBM is prefixed as ‘Light’ because of its high speed. Light GBM can handle the large size of data and takes lower memory to run. Tble his is suitable as the number of records in the dataset is about 1.2 lakhs. Another reason of why Light GBM is popular is because it focuses on accuracy of results.

Since it is based on decision tree algorithms, it splits the tree leaf wise with the best fit whereas other boosting algorithms split the tree depth wise or level wise rather than leaf-wise. So when growing on the same leaf in Light GBM, the leaf-wise algorithm can reduce more loss than the level-wise algorithm and hence results in much better accuracy which can rarely be achieved by any of the existing boosting algorithms.

![LightGBM vs Boosting](https://github.com/harsh2338/nba-prediction/blob/main/assets/report_images/tree_growth.png)

NN Pranav

GA Prajna

### Expert Opinion

... Prajna


##### References

[4] Allan Z. Maymin et al. "NBA Chemistry: Positive and Negative Synergies in Basketball", 2013
