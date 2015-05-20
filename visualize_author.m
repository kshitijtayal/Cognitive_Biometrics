[A] = csvread('author.csv',0,0);     % upload file
P = datasample(A,1000,'Replace',false)  % random sample of 1000
X = P(:,359:570);   % feature selection
dissimilarities = pdist(X,'cityblock');   % dissimilarity matrix
size(dissimilarities)
opts = statset('MaxIter',400);   % maximum number of iterations
[Y,stress] =mdscale(dissimilarities,2,'criterion','metricsstress','Options',opts);   % multidimension scaling
plot(Y(:,1),Y(:,2),'o','LineWidth',2)    
labels = round([P(:,571)]);      % different labels for different authors
display(labels)
n  = gscatter(Y(:,1),Y(:,2),labels)
xlabel('Embedded Dimension 1','FontSize',14,'Fontweight','bold')   % xlabel
ylabel('Embedded Dimension 2','FontSize',14,'Fontweight','bold')   % ylabel
hLeg = legend('n')           
set(hLeg,'visible','off')   % no legend
