[A] = csvread('finalmatrix.csv',0,0);
% P = datasample(A,1000,'Replace',false)
X = P(:,374:586);
size(X)
dissimilarities = pdist(X,'cityblock');
size(dissimilarities)
[Y,stress] =mdscale(dissimilarities,2,'criterion','metricsstress');
plot(Y(:,1),Y(:,2),'o','LineWidth',2)
labels = round([P(:,587)]);
display(labels)
gscatter(Y(:,1),Y(:,2),labels,'rb','ox+*sdv^<>ph.')
xlabel('Embedded Dimension 1','FontSize',14,'Fontweight','bold')
ylabel('Embedded Dimension 2','FontSize',14,'Fontweight','bold')
legend({'Genuine','Imposter'},'FontSize',18)

