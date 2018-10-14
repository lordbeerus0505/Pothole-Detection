Array=csvread('test.csv');
x = Array(:, 1);
y = Array(:, 2);
z = Array(:,3);

scatter(y,z)
