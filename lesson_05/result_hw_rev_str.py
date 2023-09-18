from hw_05 import  reverse_string

# TARGET FUNCTIONS
@reverse_string
def get_university_name() -> str:
  return "Western Institute of Technology and Higher Education"

@reverse_string
def get_university_founding_year() -> int:
  return 1957

# TEST OUPUT
print(
  get_university_name(),
  get_university_founding_year(),
  sep="\n"
)

