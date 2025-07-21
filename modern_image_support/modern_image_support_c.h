#ifndef MODERN_IMAGE_SUPPORT_C_H
#define MODERN_IMAGE_SUPPORT_C_H

#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdio.h>
#include <stdbool.h>

// Function declarations
bool is_webp_supported(const char *user_agent);
bool is_avif_supported(const char *user_agent);

struct browser_version {
    const char *name;
    int min_version;
    size_t name_len;
};

// WebP support versions
static const struct browser_version webp_browser_versions[] = {
    {"Firefox", 65, 7},
    {"Chrome", 32, 6},
    {"Edge", 18, 4},
    {"AppleWebKit", 605, 11},  // Safari 14
    {"OPR", 19, 3},
    {"UCBrowser", 12, 9},
    {"SamsungBrowser", 4, 14},
    {"QQBrowser", 10, 9}
};

// AVIF support versions
static const struct browser_version avif_browser_versions[] = {
    {"Firefox", 93, 7},        // Firefox 93+
    {"Chrome", 85, 6},         // Chrome 85+
    {"Edge", 85, 4},           // Edge 85+
    {"AppleWebKit", 612, 11},  // Safari 16+ (macOS 12.3+, iOS 15.4+)
    {"OPR", 71, 3},           // Opera 71+
    {"SamsungBrowser", 14, 14} // Samsung Internet 14+
};

#define WEBP_BROWSER_VERSION_COUNT (sizeof(webp_browser_versions) / sizeof(webp_browser_versions[0]))
#define AVIF_BROWSER_VERSION_COUNT (sizeof(avif_browser_versions) / sizeof(avif_browser_versions[0]))

static bool check_browser_support(const char *user_agent, const struct browser_version *versions, size_t count)
{
    if (user_agent == NULL)
    {
        return false;
    }
    
    for (size_t i = 0; i < count; i++)
    {
        const struct browser_version *current_browser = &versions[i];
        const char *found = strstr(user_agent, current_browser->name);
        if (found != NULL)
        {
            const char *version = found + current_browser->name_len;
            while (!isdigit(*version) && *version != '\0')
            {
                version++;
            }
            if (*version != '\0')
            {
                int version_number = atoi(version);
                if (version_number >= current_browser->min_version)
                {
                    return true;
                }
            }
        }
    }

    return false;
}

bool is_webp_supported(const char *user_agent)
{
    return check_browser_support(user_agent, webp_browser_versions, WEBP_BROWSER_VERSION_COUNT);
}

bool is_avif_supported(const char *user_agent)
{
    return check_browser_support(user_agent, avif_browser_versions, AVIF_BROWSER_VERSION_COUNT);
}

#endif
