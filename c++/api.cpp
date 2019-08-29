#include "api.h"
#include <iostream>

nlohmann::json::object_t ApiExample::GetJSON(cpr::Url url,
					     cpr::Parameters params) {
  auto r = cpr::Get(url, params);
  std::cout << r.text << std::endl;
  auto response = nlohmann::json::parse(r.text);
  return response;
}

nlohmann::json::object_t ApiExample::PutJSON(cpr::Url url,
					     cpr::Parameters params) {
  auto r = cpr::Put(url, params);
  auto response = nlohmann::json::parse(r.text);
  return response;
}
