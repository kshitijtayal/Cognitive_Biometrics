[A] = csvread('author.csv',0,0);
P = datasample(A,1000,'Replace',false)
X = P(:,359:570);
dissimilarities = pdist(X,'cityblock');
size(dissimilarities)
opts = statset('MaxIter',400);
[Y,stress] =mdscale(dissimilarities,2,'criterion','metricsstress','Options',opts);
plot(Y(:,1),Y(:,2),'o','LineWidth',2)
labels = round([P(:,571)]);
display(labels)
n  = gscatter(Y(:,1),Y(:,2),labels)
xlabel('Embedded Dimension 1','FontSize',14,'Fontweight','bold')
ylabel('Embedded Dimension 2','FontSize',14,'Fontweight','bold')
hLeg = legend('n')
set(hLeg,'visible','off')
