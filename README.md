# K means 

**K means** algorithm implmeneted both in `python` and `cpp`, in order to show the differences in speed of processing the data of each.

The data set is 100 points with `(x,y)` coordinates within each point.

The algorithm is explained well in [wikipedia](https://en.wikipedia.org/wiki/K-means_clustering).

<br/>


## 💻 Python algorithm
The algorithm in `python` is run via http://www.codeskulptor.org/ online `python` enviroment.

In the `Python` algorithm, as it can be seen I have circled the centers of the clusters that were found after approximately 12 iterations of the algorithm. (After 12 iterations the center of the clusters stopped changing significantly).


At the end of the run of the `Python` algorithm, an output of the results is generated (The runtime calculation does not include output production):
![VisualizationAlgo](https://user-images.githubusercontent.com/15849186/77537448-ccee0980-6ea6-11ea-9397-bd12d95a9432.PNG)

## :hourglass_flowing_sand: Runtime Diff
It is clearly seen that the `cpp` language is much faster in computing that data compared to `python`.
![timeDiff](https://user-images.githubusercontent.com/15849186/77539537-34f21f00-6eaa-11ea-8467-48067713b050.PNG)

*:warning: **Disclaimer**:* The algorithm is implemented in a very simplistic way, hence if one to implement it in a different way and get different results.


