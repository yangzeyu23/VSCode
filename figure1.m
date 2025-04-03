load data.mat;
plot(SinSquare, OmegaSquare, 'b', 'LineWidth', 2);

%设置图例位置和字体大小 
legend('Dispersion Relation', 'Location', 'northeast', 'FontSize', 12, 'FontWeight', 'bold');
xlabel('Time(s)');
ylabel('Amplitude(mVpp)');
title('Dispersion Relation of Sinusoidal Square Wave');
%绘制网格线
grid on;
%设置网格线颜色和线型
grid minor;
%设置坐标轴范围
xlim([0 0.45]);
ylim([40 240]);
%设置坐标轴刻度
set(gca, 'XTick', 0:0.05:0.45, 'YTick', 40:20:240);
%添加图片注释
%text(0.1, 200, 'Dispersion Relation of Sinusoidal Square Wave', 'FontSize', 12, 'Color', 'k', 'FontWeight', 'bold');
%设置坐标轴字体大小和颜色
set(gca, 'FontSize', 12, 'FontWeight', 'bold', 'XColor', 'k', 'YColor', 'k');
%设置图片边距
set(gca, 'Position', [0.1 0.1 0.8 0.8]);
%设置图片比例为6：4
set(gcf, 'PaperUnits', 'inches', 'PaperSize', [1 1], 'PaperPosition', [0 0 5 5]);

