% make a dy/dt vs y plot that shows steady states

clear;

% parameters
% ---

lambda = 0.5;
K = 8;  % carrying capacity
y_max = 11;  % extend beyond K to see behavior

% plot dy/dt vs y
% ---

% matlab on Linux is kooky, please leave this figure size as is
figure('Visible', 'off', 'Position', [100, 100, 100, 80]);

% plot relationship
y_range = linspace(0, y_max, 100);
dydt = lambda .* y_range .* (1 - y_range./K);
h = plot(y_range, dydt, "k--", "LineWidth", 1);
h.Color(4) = 0.1; % make faint

% line for y = 0
yline(0, "k", "LineWidth", 1);

% mark steady states
% xline(0, "r:", "LineWidth", 1);  % y = 0 steady state
% xline(K, "r:", "LineWidth", 1);  % y = K steady state

% decorate
title(sprintf("y versus dy/dt = %.1f y (1 - y/%d)", lambda, K))
xlabel("population size y")
ylabel("change in population size dy/dt")

% set axis limits to include both steady states
xlim([-0.9, y_max]);
ylim([min(dydt) - 0.2, max(dydt) + 0.2]);

exportgraphics(gcf, 'logistic_dydt.pdf', 'ContentType', 'vector', 'BackgroundColor', 'none')
