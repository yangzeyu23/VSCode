load data.mat

% 方法1：直接使用fit函数
% StartPoint 参数解释：
% [A, B, C] 分别对应拟合函数 A*sin(B*x + C) 中的振幅(A)、频率(B)、相位(C)
[fitResult, gof] = fit(n, Am_2, 'sin1', 'StartPoint', [330, 1, 0], 'MaxIter', 2000); 
% 确保返回 gof
plot(fitResult, 'r-'); % 使用默认绘图设置绘制拟合曲线，并将曲线设置为红色
hold on; % 保持当前图窗
plot(n, Am_2, 'ro'); % 使用红色圆圈标注数据点
hold off; % 释放图窗
grid on; % 添加网格线

% 设置图形标题
title('Amplitude(Vpp) depending on the number, at frequency as 1.0275Hz');

ax = gca; % 获取当前坐标轴
ax.XTick = min(n):1:max(n); % 设置 x 轴单位为 1
ax.YTick = -400:50:350; % 设置 y 轴单位为 50，范围为 -400 到 350
ax.YLim = [-400, 400]; % 设置 y 轴范围

% 设置坐标轴标签
xlabel('n'); % 设置 x 轴标签
ylabel('Amplitude for 1.275Hz (mV)'); % 设置 y 轴标签



% 显示拟合结果的详细信息，包括拟合系数和相关系数
disp(fitResult);
disp(['R-square: ', num2str(gof.rsquare)]);

% 在图中添加拟合系数和相关系数信息
coeffs = coeffvalues(fitResult); % 获取拟合系数
rsquare = gof.rsquare; % 获取相关系数
text(mean(n), max(Am_2) * 0.9, ... % 调整位置以确保信息显示在图中
    sprintf('A=%.2f, B=%.2f, C=%.2f\nR^2=%.4f', coeffs(1), coeffs(2), coeffs(3), rsquare), ...
    'HorizontalAlignment', 'center', 'BackgroundColor', 'white');

% 使用命令行打开app曲线拟合器，指定数据集和拟合类型
% 指定使用三角函数拟合
% 设置迭代起始位置和迭代次数
%curveFitter(n, Am_2, 'FitType', 'sin1', 'StartPoint', [1, 1, 0], 'MaxIter', 1000);