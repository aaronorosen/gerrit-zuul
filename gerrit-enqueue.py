import argparse
import getpass

import zuul.rpcclient
from gerritlib import gerrit


def main():

    parser = argparse.ArgumentParser("Zuul/gerrit patch enqueuer")
    parser.add_argument("project", type=str, help="Name of project")
    parser.add_argument("zuul_server", type=str,
                        help="ip address of zuul server.")
    parser.add_argument("--zuul-port", type=int, default=4730,
                        help="zuul port")
    parser.add_argument("--gerrit-url", type=str,
                        default="review.openstack.org",
                        help="ip address of gerrit server")
    parser.add_argument("--gerrit-user", type=str, default=getpass.getuser(),
                        help="gerrit user")
    parser.add_argument("--gerrit-port", type=int, default=29418,
                        help="gerrit user")
    parser.add_argument("--zuul-trigger", type=str, default='gerrit',
                        help="gerrit trigger")
    parser.add_argument("--zuul-pipeline", type=str, default='check',
                        help="gerrit check")

    args = parser.parse_args()
    client = gerrit.Gerrit(hostname=args.gerrit_url,
                           username=args.gerrit_user,
                           port=args.gerrit_port)
    zuul_client = zuul.rpcclient.RPCClient(args.zuul_server, args.zuul_port)
    query = "--current-patch-set status:open project:%s" % args.project
    results = client.bulk_query(query)
    for result in results:
        if 'rowCount' in result:
            # this is the last element in the json body so we break
            # out of it here.
            break
        print ("enqueuing: %s" % result['url'])
        change = ("%s,%s" % (result['number'],
                             result['currentPatchSet']['number']))
        zuul_client.enqueue(pipeline=args.zuul_pipeline,
                            project=args.project,
                            trigger=args.zuul_trigger,
                            change=change)


main()
