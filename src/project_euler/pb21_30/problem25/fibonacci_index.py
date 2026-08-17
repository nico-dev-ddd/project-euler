def index_first_term_with_n_digits(n_digits: int) -> int:
    current_term, next_term = 1, 1
    index = 1
    while len(str(current_term)) < n_digits:
        current_term, next_term = next_term, current_term + next_term
        index += 1
    return index


if __name__ == "__main__":
    print(index_first_term_with_n_digits(1000))
