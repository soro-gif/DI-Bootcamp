import math


class Pagination:

    # ── Étape 2 : constructeur ──────────────────────────────
    def __init__(self, items=None, page_size=10):
        self.items       = items if items is not None else []
        self.page_size   = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / page_size)

    # ── Étape 3 : éléments visibles ────────────────────────
    def get_visible_items(self):
        start = self.current_idx
        end   = start + self.page_size
        return self.items[start:end]

    # ── Étape 4 : navigation ───────────────────────────────
    def go_to_page(self, page_num):
        if not (1 <= page_num <= self.total_pages):
            raise ValueError(
                f"Page {page_num} invalide. Choisissez entre 1 et {self.total_pages}."
            )
        self.current_idx = (page_num - 1) * self.page_size

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = (self.total_pages - 1) * self.page_size
        return self

    def next_page(self):
        if self.current_idx + self.page_size < len(self.items):
            self.current_idx += self.page_size
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= self.page_size
        return self

    # ── Bonus : __str__ ────────────────────────────────────
    def __str__(self):
        return "\n".join(str(item) for item in self.get_visible_items())


# ── Tests ──────────────────────────────────────────────────
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())          # ['a','b','c','d']
p.next_page()
print(p.get_visible_items())          # ['e','f','g','h']
p.last_page()
print(p.get_visible_items())          # ['y','z']

# Bonus : chaînage de méthodes
p.first_page()
print(p.next_page().next_page().next_page().get_visible_items())
# ['m','n','o','p']

# ValueError attendue
try:
    p.go_to_page(10)
except ValueError as e:
    print(e)