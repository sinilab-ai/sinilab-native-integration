#pragma once
#include <chrono>
#include <cstdint>
#include <functional>
#include <mutex>
#include <string>

namespace sinilab {
enum class Status { ActivationRequired, Licensed, OfflineGrace, ValidationRequired, Revoked };
enum class ResponseKind { Active, Rejected, NetworkUnavailable };
struct Response { ResponseKind kind; std::string bridgeCode; };
struct Snapshot {
    Status status = Status::ActivationRequired;
    bool allowed = false;
    std::string reason;
};
// The caller supplies a Bridge adapter and persisted timestamps/credentials.
// Never treat this state machine alone as proof of a valid licence.
class LicensingPolicy {
public:
    using Clock = std::chrono::system_clock;
    using TimePoint = Clock::time_point;
    static constexpr auto CacheDuration = std::chrono::minutes(15);
    static constexpr auto OfflineGraceDuration = std::chrono::hours(24);
    void restore(bool hasCredential, bool knownRevoked, TimePoint lastOnlineSuccess);
    Snapshot evaluate(TimePoint now) const;
    void apply(const Response& response, TimePoint now);
    bool shouldRefresh(TimePoint now) const;
private:
    mutable std::mutex mutex_;
    bool credential_ = false;
    bool revoked_ = false;
    bool offline_ = false;
    TimePoint lastOnline_{};
};
} // namespace sinilab
