#include "api.h"

#include <iostream>
#include <string>
#include <bits/stdc++.h>
#include <regex>

bool replace(std::string& str, const std::string& from, const std::string& to) {
    size_t start_pos = str.find(from);
    if(start_pos == std::string::npos)
        return false;
    str.replace(start_pos, from.length(), to);
    return true;
}

int main(int argc, char** argv) {

  // Input string
  std::string query = R"(MASTERCARD
Auth Code: 759830
Merchand ID: 887
Account Number: ************3456
Expiry: 08/12
NO CARDHOLDER VERIFICATION
)";

  // card number regex ([x*]{4}|([0-9]{4}))[x*]{8}([0-9]{4})
  const std::regex card_regex("([x*]{4}|([0-9]{4}))[x*]{8}([0-9]{4})");
  std::smatch card_number;
  
  // date regex \s([0-9]{2}\/[0-9]{2})\s
  const std::regex date_regex("\\s([0-9]{2}/[0-9]{2})\\s");
  std::smatch card_date;
  
  std::regex_search(query, card_number, card_regex);
  std::regex_search(query, card_date, date_regex);

  ApiExample api;
  auto url = cpr::Url("http://localhost:8080/api/customer");

  std::string end_date = card_date.str(1);
  replace(end_date,"/",".20");

  cpr::Parameters param;
  param.AddParameter(cpr::Parameter("trailing_digits",card_number.str(3)));
  param.AddParameter(cpr::Parameter("end_date",end_date));
  
  if (card_number.str(2) != ""){
    param.AddParameter(cpr::Parameter("leading_digits",card_number.str(2)));  
  }
  
  std::cout << api.GetJSON(url,param)["matches"] << std::endl;
  


  std::string name;
  std::string email;

  std::cin >> name;
  std::cin >> email;


  param.AddParameter(cpr::Parameter("first_name",name));
  param.AddParameter(cpr::Parameter("email",email));

  api.PutJSON(url,param);
 
  
  

  
  return 0;
}
