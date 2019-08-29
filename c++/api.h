#pragma once

#include <nlohmann/json.hpp>
#include <cpr/cpr.h>
#include <string>

struct ApiExample {
  nlohmann::json::object_t GetJSON(cpr::Url url,
				   cpr::Parameters params);

  nlohmann::json::object_t PutJSON(cpr::Url url,
				   cpr::Parameters params);
};
