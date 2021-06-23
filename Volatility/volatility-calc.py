from qiime2 import Artifact, Metadata
from skbio.stats.distance import DistanceMatrix
import pandas as pd
import numpy as np

study_id = "studyid"
timepoint = "month-of-life"

metadata = Metadata.load("sample_data/ecam-sample-metadata.tsv")
distmat = Artifact.load("sample_data/unweighted_unifrac_distance_matrix.qza")


def find_previous_distances(metadata: Metadata, distance_matrix: Artifact, study_id: str, timepoint: str):
    """metadata: Metadata file containing study_id and timepoint variables
        distance_matrix: Artifact containing the Distance Matrix
        study_id: name of column containing participant or site id
        timepoint: name of column containing the timepoint"""    
    
    #convert to dataframes
    metadata = metadata.to_dataframe()
    distmat = distance_matrix.view(DistanceMatrix).to_data_frame()

    #create a sorted index based on study id then sorted by ascending timepoint
    sorted_index = metadata.sort_values([study_id, timepoint]).index

    #sort the distance matrix by this sorted index
    distmat = distmat.reindex(index = sorted_index, 
                              columns = sorted_index)

    #replace all rows with the first timepoint for each study id with NaN
    #doing this because there is no distance to previous
    distmat.loc[metadata.groupby(study_id)[timepoint].idxmin(), :] = np.NaN
    
    #convert to matrix for quick and easy indexing
    distmat = np.matrix(distmat)
    size = distmat.shape[0]

    #grab distance from each to the next timepoint
    prev_distances = [distmat[i+1,i] for i in range(size-1)]
    #first one must be NaN
    prev_distances.insert(0, np.NaN)

    #turn into a Series
    prev_distances = pd.Series(prev_distances, index=sorted_index)
    
    return prev_distances

#test_prev_distances = find_previous_distances(metadata, distmat, study_id, timepoint)
#print(test_prev_distances)