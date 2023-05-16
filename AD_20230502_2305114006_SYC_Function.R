# y <- log(100)
# y

# d <- c(1, 7, 4, 2, 3)
# sort(d)
# sort(d, decreasing = TRUE)
# sort(d, FALSE)

# str <- paste('I am', 'hungry', sep = ' & ')
# str

# a <- '나의 나이는'
# b <- '20'
# c <- '입니다'
# paste(a, b, c, sep = ' ')

# a <- 1 : 12
# b <- '월'
# c <- paste(a, b, sep = '')
# c

sales <- c(750, 740, 760, 680, 700, 710, 850, 890, 700, 720, 690, 730)
names(sales) <- paste(1 : 12, '월', sep = '')
sales

sales['7월']

sales[1] + sales[4]
max_month <- sort(sales, decreasing = T)
max_month[1]

sum(sales[1 : 6])
sales[1 : 6]
mean(sales[1 : 6])
min(sales[1 : 6])
max(sales[1 : 6])
