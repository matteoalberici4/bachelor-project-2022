# plotter.py

# Copyright 2022 Matteo Alberici
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for
# the specific language governing permissions and limitations under the License.

from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    
    # Defining the name of the benchmark
    benchmark = input()

    # Assigning the areas with respect to the error thresholds
    points1 = []
    points2 = []
    points3 = []
    points4 = []
    points5 = []
    points6 = []

    # Creating a figure
    fig, ax = plt.subplots()

    # Defining the error thresholds
    x = np.array([])

    # Defining the minimum area values for each error threshold
    y = np.array([])

    # Writing the minimal areas labels
    for i in range(len(x)):
        plt.annotate(f'{y[i]}', (x[i], y[i]+2), ha='center')

    # Plotting the areas defined for each error threshold
    plt.scatter(x, y, color='#228bc2')
    x_ = [x[1] for i in range(len(points1))]
    plt.scatter(x_, points1, color='#228bc2')
    x_ = [x[2] for i in range(len(points2))]
    plt.scatter(x_, points2, color='#228bc2')
    x_ = [x[3] for i in range(len(points3))]
    plt.scatter(x_, points3, color='#228bc2')
    x_ = [x[4] for i in range(len(points4))]
    plt.scatter(x_, points4, color='#228bc2')
    x_ = [x[5] for i in range(len(points5))]
    plt.scatter(x_, points5, color='#228bc2')
    x_ = [x[6] for i in range(len(points6))]
    plt.scatter(x_, points6, color='#228bc2')
    
    # Plotting the Graph
    plt.plot(x, y)
    plt.title(f'Mustool Minimal Areas: {benchmark}')
    plt.xlabel('Error Thresholds')
    plt.ylabel('Minimal Areas')
    plt.show()

    fig.savefig(f'{benchmark}.pdf', dpi=120)
