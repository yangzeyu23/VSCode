load data.mat;
x=[572  484   408 336     270 220 196 174 154 138 124 116   110  105 101]';
plot(n,x,'-o','LineWidth',2,'MarkerSize',3,'MarkerFaceColor','b','MarkerEdgeColor','b');
xlabel('n','FontSize',12,'FontWeight','bold','Color','k');
ylabel('Amplitude (mV)','FontSize',12,'FontWeight','bold','Color','k');
title('Amplitude Decay Image','FontSize',12,'FontWeight','bold','Color','k');
grid on;
set(gca, 'XTick', 0:1:14, 'YTick', 100:50:600);