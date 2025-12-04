% y_{n+1} = G(y_n) where G'(fixed_point) has specified slope

% Parameters
slope = 1;           % Change this to -0.5 or -1.25
fixed_point = 4;       % Fixed point location
y0 = 4;               % Starting value
n_iterations = 0;     % Number of iterations
y_max = 8;
x_max = 8;

% Define the linear function G(y) = slope*(y - fixed_point) + fixed_point
G = @(y) slope * (y - fixed_point) + fixed_point;

% plot
figure('Visible', 'off', 'Position', [100, 100, 100, 80]);
hold on;
axis equal;
xlim([0 x_max]);
ylim([0 y_max]);

% Plot y = x line (diagonal)
x_line = 0:0.1:x_max;
plot(x_line, x_line, 'k-', 'LineWidth', 1);

% Plot G(y) function
y_vals = 0:0.1:y_max;
plot(y_vals, G(y_vals), 'b-', 'LineWidth', 2);

% Cobweb iteration
y = y0;
for i = 1:n_iterations
    y_next = G(y);

    % Vertical line from (y, y) to (y, G(y))
    h = plot([y y], [y y_next], 'k-', 'LineWidth', 1);
    h.Color(4) = 0.1; % make faint

    % Horizontal line from (y, G(y)) to (G(y), G(y))
    h = plot([y y_next], [y_next y_next], 'k-', 'LineWidth', 1);
    h.Color(4) = 0.1; % make faint

    y = y_next;
end

xticks(0:x_max);
yticks(0:y_max);

xlabel('y_n', 'Position', [8, -0.5]);  % Adjust second value for vertical position
ylabel('y_{n+1}', 'Position', [-0.5, 8], 'Rotation', 0);  % Rotation=0 makes it horizontal

title("G'(y) = 1");
% legend('y_{n+1} = y_n', 'G(y)', '', 'Location', 'best');
set(gca, 'XTickLabel', []);
set(gca, 'YTickLabel', []);
grid on;

exportgraphics(gcf, 'cobweb_pos1.pdf', 'ContentType', 'vector', 'BackgroundColor', 'none')
