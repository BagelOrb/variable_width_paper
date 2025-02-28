'overlap compensated'
data = [[3500.02, 525.62, 500  ],
 [13749.69, 0, 500      ],
 [13749.69, 0, 0        ],
 [3500.02, -525.62, 500 ],
 [2500.02, 1576.87, 500 ],
 [34037.46, 0, 500      ],
 [34037.46, 0, 0        ],
 [24049.96, -499.38, 500],
 [2500.02, -1576.87, 500],
 [1500.01, 2628.12, 500 ],
 [54062.43, 0, 500      ],
 [54062.43, 0, 0        ],
 [44074.91, 499.38, 500 ],
 [1500.01, -2628.12, 500],
 [500.00, 3679.37, 500  ],
 [74087.39, 0, 500      ],
 [74087.39, 0, 0        ],
 [64099.88, 499.38, 500 ],
 [500.00, -3679.37, 500 ]]
d=np.array(data)



'my algorithm'
>>> data = [[3500.02, 525.62, 500   ],
...  [23860.08, 360.72, 363  ],
...  [24025.0, 0.0, 363      ],
...  [23860.08, -360.72, 363 ],
...  [3500.02, -525.62, 500  ],
...  [2500.02, 1576.87, 500  ],
...  [24581.51, 1082.15, 367 ],
...  [25022.63, 472.02, 473  ],
...  [43846.44, 322.12, 325  ],
...  [44049.95, 0, 325       ],
...  [43846.44, -322.12, 325 ],
...  [25022.63, -472.02, 473 ],
...  [24581.51, -1082.15, 367],
...  [2500.02, -1576.87, 500 ],
...  [1500.01, 2628.12, 500  ],
...  [25302.95, 1803.59, 372 ],
...  [25967.57, 1416.96, 484 ],
...  [44490.54, 966.22, 330  ],
...  [45046.10, 470.53, 475  ],
...  [63793.94, 244.65, 247  ],
...  [64074.91, 0, 247       ],
...  [63793.94, -244.65, 247 ],
...  [45046.10, -470.53, 475 ],
...  [44490.54, -966.22, 330 ],
...  [25967.57, -1416.96, 484],
...  [25302.95, -1803.59, 372],
...  [1500.01, -2628.12, 500 ],
...  [500.0, 3679.37, 500    ],
...  [26024.38, 2525.02, 376 ],
...  [26913.38, 2362.77, 492 ],
...  [45134.51, 1610.19, 335 ],
...  [45987.15, 1411.58, 487 ],
...  [64283.23, 733.95, 253  ],
...  [65064.80, 464.27, 476  ],
...  [73812.67, 250.91, 257  ],
...  [74087.39, 0, 257       ],
...  [73812.67, -250.91, 257 ],
...  [65064.80, -464.27, 476 ],
...  [64283.23, -733.95, 253 ],
...  [45987.15, -1411.58, 487],
...  [45134.51, -1610.19, 335],
...  [26913.38, -2362.77, 492],
...  [26024.38, -2525.02, 376],
...  [500.0,    -3679.37, 500]]




plt.figure()
plt.plot(d[:,0], d[:,1])
fig = plt.gcf()
ax = fig.gca()
for [x,y,w] in data:
  ax.add_artist(plt.Circle((x, y), w, color='r'))

plt.show()

