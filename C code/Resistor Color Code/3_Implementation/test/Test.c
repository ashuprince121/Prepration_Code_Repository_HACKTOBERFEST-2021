#include "unity.h"
#include "inc/header.h"

/* Modify these two lines according to the project */
#include "inc/header.h"
#define PROJECT_NAME    "Code"

/* Prototypes for all the test functions */
void test_search(void);
void test_match(void);

/* Required by the unity test framework */
void setUp(){}
/* Required by the unity test framework */
void tearDown(){}

/* Start of the application test */
int main()
{
/* Initiate the Unity Test Framework */
  UNITY_BEGIN();

/* Run Test functions */
  RUN_TEST(test_search);
  RUN_TEST(test_match);

  /* Close the Unity Test Framework */
  return UNITY_END();
}

/* Test cases */

void test_search(void)
{
    TEST_ASSERT_EQUAL(0, Color("BLACK"));

}

void test_match(void)
{
    TEST_ASSERT_EQUAL(1, CompareMatch("BLACK","BLACK"));

}