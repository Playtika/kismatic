from ansible import errors

# Returns the name of the container image that should be used
# depending on whether a private registry is being used.
def final_image(upstream_image, registry_url = '', private = False):
    if not private:
        return upstream_image
    if registry_url == '':
        raise errors.AnsibleFilterError('Must pass registry url when using private registry.')

    # Playtika workaround for Artifactory as docker registry
    registry = ['quay.io','gcr.io']
    if upstream_image.split('/', 1)[0]  not in registry:
      return registry_url + "/" + upstream_image
    else:
      return registry_url + "/" + upstream_image.split('/', 1)[-1]

class FilterModule(object):
    filter_map = {
        'final_image': final_image
    }

    def filters(self):
        return self.filter_map
